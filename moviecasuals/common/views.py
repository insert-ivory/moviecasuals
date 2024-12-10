from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView

from moviecasuals.director.models import Director
from moviecasuals.mixins import AccessControlMixin
from moviecasuals.movie.forms import UpdateCommentForm, DeleteCommentForm
from moviecasuals.movie.models import Movie, Comment, Rating
from django.db.models import Q, Avg


class HomePageView(ListView):
    template_name = 'common/homepage.html'
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_ratings = Rating.objects.filter(user=self.request.user)
            user_ratings_dict = {rating.movie.id: rating.rating for rating in user_ratings}
            context['user_ratings'] = user_ratings_dict
        else:
            context['user_ratings'] = {}
        return context


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        movie_id = kwargs.get("pk")
        movie = get_object_or_404(Movie, id=movie_id)
        text = request.POST.get("text")

        if text:
            comment = Comment.objects.create(user=request.user, movie=movie, text=text)

            return JsonResponse({
                'id': comment.id,
                'text': comment.text,
                'username': comment.user.username,
                'created_at': comment.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
            })

        return JsonResponse({'error': 'Invalid data'}, status=400)


class EditCommentView(LoginRequiredMixin, AccessControlMixin, UpdateView):
    template_name = 'movie/edit_comment.html'
    pk_url_kwarg = 'pk'
    model = Comment
    form_class = UpdateCommentForm
    success_url = reverse_lazy('homepage')


class DeleteCommentView(LoginRequiredMixin, AccessControlMixin, DeleteView):
    pk_url_kwarg = 'pk'
    template_name = 'movie/delete_comment.html'
    success_url = reverse_lazy('homepage')
    form_class = DeleteCommentForm
    model = Comment

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class AccessControlView(TemplateView):
    template_name = 'common/no_permission.html'


class SearchBarView(ListView):
    template_name = 'common/searchbar.html'
    queryset = Movie.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('searched-word')
        if query:
            movies = Movie.objects.filter(Q(title__icontains=query)).distinct()
            directors = Director.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            ).distinct()
            print(directors)
            context['movies'] = movies
            context['directors'] = directors
        else:
            context['movies'] = Movie.objects.none()
            context['directors'] = Director.objects.none()
        return context


class GiveRatingView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        movie_id = kwargs.get("movie_id")
        selected_rating = request.POST.get("rating")

        if not selected_rating or not selected_rating.isdigit() or not (1 <= int(selected_rating) <= 5):
            return JsonResponse({'error': 'Invalid rating value'}, status=400)

        movie = get_object_or_404(Movie, id=movie_id)

        rating, created = Rating.objects.update_or_create(
            movie=movie,
            user=request.user,
            defaults={'rating': int(selected_rating)}
        )

        new_average_rating = movie.ratings.aggregate(Avg('rating'))['rating__avg'] or 0

        user_rating = movie.ratings.filter(user=request.user).first().rating if movie.ratings.filter(
            user=request.user).exists() else None

        return JsonResponse({
            'message': 'Rating added successfully',
            'new_average_rating': round(new_average_rating, 2),
            'user_rating': user_rating
        })

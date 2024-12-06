from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from moviecasuals.movie.forms import UpdateCommentForm, DeleteCommentForm
from moviecasuals.movie.models import Movie, Comment


class HomePageView(ListView):
    template_name = 'common/homepage.html'
    model = Movie
    context_object_name = 'movies'


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        movie_id = kwargs.get("movie_id")
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


class EditCommentView(LoginRequiredMixin, UpdateView):
    template_name = 'movie/edit_comment.html'
    pk_url_kwarg = 'pk'
    model = Comment
    form_class = UpdateCommentForm
    success_url = reverse_lazy('homepage')


class DeleteCommentView(DeleteView):
    pk_url_kwarg = 'pk'
    template_name = 'movie/delete_comment.html'
    success_url = reverse_lazy('homepage')
    form_class = DeleteCommentForm
    model = Comment

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)



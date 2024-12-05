from django import forms

from moviecasuals.movie.models import Movie, Comment


class BaseMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['approved']


class CreateMovieForm(BaseMovieForm):
    pass


class BaseCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class UpdateCommentForm(BaseCommentForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        ),
        required=True
    )


class DeleteCommentForm(BaseCommentForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        ),
        required=True
    )
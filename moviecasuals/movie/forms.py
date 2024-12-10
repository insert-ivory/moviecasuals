from django import forms

from moviecasuals.director.models import Director
from moviecasuals.movie.models import Movie, Comment


class BaseMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['approved', 'user']


class CreateMovieForm(BaseMovieForm):
    director = forms.CharField(
        label="Director",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Write the Director's full name"
        }),
        error_messages={
            'required': "Please make sure to provide the director's full name."
        }
    )

    class Meta(BaseMovieForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Movie's Title..."}),
            'genre_choices': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': "Movie's description..."}),
            'picture_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image url...'}),
        }

    def clean_director(self):
        director_name = self.cleaned_data.get('director')
        try:
            first_name, last_name = director_name.split(' ', 1)
            director = Director.objects.get(first_name=first_name, last_name=last_name)
        except (ValueError, Director.DoesNotExist):
            raise forms.ValidationError("Both names should match an already existing director.")
        return director

    def save(self, commit=True):
        movie = super().save(commit=False)
        movie.director = self.cleaned_data['director']
        if commit:
            movie.save()
        return movie

class EditMovieForm(BaseMovieForm):
    class Meta(BaseMovieForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write the title of the movie'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Description should not exceed 2000 characters.'
            }),

            'picture_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the picture URL of the movie'
            }),

            'genre_choices': forms.Select(attrs={
                'class': 'form-select'
            }),
            'director': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


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
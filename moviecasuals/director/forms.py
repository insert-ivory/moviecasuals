from django import forms

from moviecasuals.director.models import Director


class BaseDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = ['user', 'approved',]

class EditDirectorForm(BaseDirectorForm):
    pass


class MovieUserCreateDirectorForm(BaseDirectorForm):
    class Meta(BaseDirectorForm.Meta):
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Director's First Name. . ."}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Director's Last Name. . ."}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': "Director's Bio. . ."}),
            'picture_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image url. . .'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
        labels = {
            'date_of_birth': 'Date of Birth'
        }

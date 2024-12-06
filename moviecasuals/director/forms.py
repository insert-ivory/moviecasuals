from django import forms

from moviecasuals.director.models import Director


class BaseDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = ['user',]

class EditDirectorForm(BaseDirectorForm):
    pass
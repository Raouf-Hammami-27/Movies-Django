from django import forms

from films.models import Favori


class FavoriForm(forms.ModelForm):

    class Meta:
        model = Favori
        fields = ['comment']
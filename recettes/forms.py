from django import forms
from .models import Recette, Commentaire, Avis, Suggestion

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['titre', 'ingredients', 'etapes']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['pseudo', 'texte']

class AvisForm(forms.ModelForm):
    note = forms.ChoiceField(choices=[(i, i) for i in range(1, 6)], widget=forms.Select(), label="Note")

    class Meta:
        model = Avis
        fields = ['pseudo', 'note']

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['pseudo', 'description']

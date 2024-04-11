from django.shortcuts import render
from .models import Recette

def liste_recettes(request):
    recettes = Recette.objects.all()  # Récupère toutes les recettes de la base de données
    return render(request, 'recettes/liste_recettes.html', {'recettes': recettes})

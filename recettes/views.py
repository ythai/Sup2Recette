from django.shortcuts import render, redirect
from .models import Recette
from .forms import RecetteForm

def liste_recettes(request):
    recettes = Recette.objects.all()  # Récupère toutes les recettes de la base de données
    return render(request, 'recettes/liste_recettes.html', {'recettes': recettes})

def ajouter_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm()
    return render(request, 'recettes/ajouter_recette.html', {'form': form})
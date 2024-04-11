from django.shortcuts import render, redirect, get_object_or_404
from .models import Recette
from .forms import RecetteForm
from django.views.decorators.http import require_POST

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

def detail_recette(request, recette_id):
    recette = get_object_or_404(Recette, pk=recette_id)
    return render(request, 'recettes/detail_recette.html', {'recette': recette})

@require_POST
def supprimer_recette(request, recette_id):
    recette = get_object_or_404(Recette, pk=recette_id)
    recette.delete()
    return redirect('liste_recettes')

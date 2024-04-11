from django.shortcuts import render, redirect, get_object_or_404
from .models import Recette
from .forms import RecetteForm, CommentaireForm, AvisForm
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
    commentaires = recette.commentaires.all()
    avis = recette.avis.all()
    
    if request.method == 'POST':
        if 'submit_commentaire' in request.POST:
            commentaire_form = CommentaireForm(request.POST)
            if commentaire_form.is_valid():
                commentaire = commentaire_form.save(commit=False)
                commentaire.recette = recette
                # Supprime ou ajuste cette ligne car tu n'as pas de champ 'auteur'
                # commentaire.auteur = request.user
                commentaire.save()
                return redirect('detail_recette', recette_id=recette_id)
        elif 'submit_avis' in request.POST:
            avis_form = AvisForm(request.POST)
            if avis_form.is_valid():
                avis_instance = avis_form.save(commit=False)
                avis_instance.recette = recette
                # Supprime ou ajuste cette ligne
                # avis_instance.auteur = request.user
                avis_instance.save()
                return redirect('detail_recette', recette_id=recette_id)
    else:
        commentaire_form = CommentaireForm()
        avis_form = AvisForm()

    context = {
        'recette': recette,
        'commentaires': commentaires,
        'avis': avis,
        'commentaire_form': commentaire_form,
        'avis_form': avis_form,
    }
    return render(request, 'recettes/detail_recette.html', context)


@require_POST

def supprimer_recette(request, recette_id):
    recette = get_object_or_404(Recette, pk=recette_id)
    recette.delete()
    return redirect('liste_recettes')

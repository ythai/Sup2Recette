from django.db import models
from django.contrib.auth.models import User

class Recette(models.Model):
    titre = models.CharField(max_length=100)
    ingredients = models.TextField()
    etapes = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='commentaires')
    pseudo = models.CharField(max_length=100, default='anonymous')
    texte = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commentaire par {self.pseudo} sur {self.recette}'

class Avis(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='avis')
    pseudo = models.CharField(max_length=100, default='anonymous')
    note = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avis par {self.pseudo} sur {self.recette} - Note : {self.note}'
    
class Suggestion(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name='suggestions')
    pseudo = models.CharField(max_length=100, default='anonymous')
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suggestion de {self.pseudo} pour {self.recette}"


class Preference(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    preferences = models.ManyToManyField(Recette)

    def __str__(self):
        return f"Préférences de {self.utilisateur}"

from django.db import models

class Recette(models.Model):
    titre = models.CharField(max_length=100)
    ingredients = models.TextField()
    etapes = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

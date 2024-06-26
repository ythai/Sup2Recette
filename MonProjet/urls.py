"""
URL configuration for MonProjet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recettes import views as recettes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recettes/', recettes_views.liste_recettes, name='liste_recettes'),
    path('ajouter/', recettes_views.ajouter_recette, name='ajouter_recette'),
    path('recettes/<int:recette_id>/', recettes_views.detail_recette, name='detail_recette'),
    path('supprimer/<int:recette_id>/', recettes_views.supprimer_recette, name='supprimer_recette'),
]

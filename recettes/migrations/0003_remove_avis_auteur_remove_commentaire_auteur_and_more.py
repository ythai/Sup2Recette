# Generated by Django 5.0.4 on 2024-04-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0002_avis_commentaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='auteur',
        ),
        migrations.AddField(
            model_name='avis',
            name='pseudo',
            field=models.CharField(default='anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='pseudo',
            field=models.CharField(default='anonymous', max_length=100),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0004_preference_suggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avis',
            name='note',
            field=models.TextField(),
        ),
    ]
# Generated by Django 4.0.6 on 2022-11-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_produitapropos_produitactualite'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitserveur',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]

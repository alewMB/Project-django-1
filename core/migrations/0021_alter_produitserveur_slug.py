# Generated by Django 4.0.6 on 2022-11-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_formation_slug_produitactualite_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produitserveur',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

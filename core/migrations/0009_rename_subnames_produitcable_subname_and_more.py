# Generated by Django 4.0.6 on 2022-07-22 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_produitcable_subnames_produitcamera_subnames_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produitcable',
            old_name='subnames',
            new_name='subname',
        ),
        migrations.RenameField(
            model_name='produitcamera',
            old_name='subnames',
            new_name='subname',
        ),
        migrations.RenameField(
            model_name='produitelephone',
            old_name='subnames',
            new_name='subname',
        ),
        migrations.RenameField(
            model_name='produitroute',
            old_name='subnames',
            new_name='subname',
        ),
        migrations.RenameField(
            model_name='produitserveur',
            old_name='subnames',
            new_name='subname',
        ),
        migrations.RenameField(
            model_name='produitserveurappel',
            old_name='subnames',
            new_name='subname',
        ),
        migrations.RenameField(
            model_name='produitswitch',
            old_name='subnames',
            new_name='subname',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_image_produitcable_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitcable',
            name='subnames',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produitcamera',
            name='subnames',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produitelephone',
            name='subnames',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produitroute',
            name='subnames',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produitserveur',
            name='subnames',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produitserveurappel',
            name='subnames',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produitswitch',
            name='subnames',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]

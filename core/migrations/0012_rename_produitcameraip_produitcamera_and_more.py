# Generated by Django 4.0.6 on 2022-07-25 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_produitcamera_produitcameraip_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='produitcameraip',
            new_name='produitcamera',
        ),
        migrations.DeleteModel(
            name='produitcameratpz',
        ),
    ]

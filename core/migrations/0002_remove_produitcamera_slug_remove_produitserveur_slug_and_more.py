# Generated by Django 4.0.6 on 2022-07-17 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produitcamera',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='produitserveur',
            name='slug',
        ),
        migrations.AlterField(
            model_name='produitcamera',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='produitserveur',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.CreateModel(
            name='produitransmissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('detail', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='produitelephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('detail', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.category')),
            ],
        ),
    ]
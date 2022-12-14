# Generated by Django 4.0.6 on 2022-11-02 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_produitservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitAPropos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subname', models.CharField(max_length=250)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('detail', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitActualite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subname', models.CharField(max_length=250)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('detail', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.category')),
            ],
        ),
    ]

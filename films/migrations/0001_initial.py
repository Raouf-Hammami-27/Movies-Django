# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 11:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_sortie', models.DateField(auto_now_add=True)),
                ('disponible', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='photos')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='films.Genre'),
        ),
    ]

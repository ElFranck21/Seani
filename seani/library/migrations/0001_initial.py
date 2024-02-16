# Generated by Django 5.0.2 on 2024-02-09 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre del modulo')),
                ('description', models.CharField(max_length=150, verbose_name='Description del modulo')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Texto de la pregunta')),
                ('image_text', models.ImageField(blank=True, null=True, upload_to='questions', verbose_name='Imagen de la pregunta')),
                ('answer1', models.CharField(max_length=150, verbose_name='Respuesta A')),
                ('answer2', models.CharField(max_length=150, verbose_name='Respuesta B')),
                ('answer3', models.CharField(blank=True, max_length=150, null=True, verbose_name='Respuesta C')),
                ('answer4', models.CharField(blank=True, max_length=150, null=True, verbose_name='Respuesta D')),
                ('correct', models.CharField(max_length=5, verbose_name='Respuesta correcta')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module')),
            ],
        ),
    ]

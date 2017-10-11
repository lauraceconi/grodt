# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('descricao', models.TextField()),
                ('nota', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('horario', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=50)),
                ('professor', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='go.Usuario'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='go.Turma'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='go.Usuario'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='go.Turma'),
        ),
    ]
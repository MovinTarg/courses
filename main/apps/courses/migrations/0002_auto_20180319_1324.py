# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.AddField(
            model_name='description',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='description', to='courses.Course'),
        ),
    ]

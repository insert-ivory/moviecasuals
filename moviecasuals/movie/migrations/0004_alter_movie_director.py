# Generated by Django 5.1.3 on 2024-12-11 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0003_alter_director_first_name_alter_director_last_name'),
        ('movie', '0003_alter_movie_user_movieuserchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='director.director'),
        ),
    ]

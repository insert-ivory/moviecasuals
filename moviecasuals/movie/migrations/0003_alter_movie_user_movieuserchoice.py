# Generated by Django 5.1.3 on 2024-12-09 13:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_genre_choices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MovieUserChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(choices=[('Unspecified', 'Unspecified'), ('Want to Watch', 'Want to Watch'), ('Watched', 'Watched'), ('Need to Rewatch', 'Need to Rewatch'), ('Interested', 'Interested'), ('Not Interested', 'Not Interested'), ('Recommended', 'Recommended')], default='Unspecified', max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_options', to='movie.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_options', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'movie')},
            },
        ),
    ]
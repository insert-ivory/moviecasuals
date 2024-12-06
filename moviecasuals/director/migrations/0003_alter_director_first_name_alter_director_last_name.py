# Generated by Django 5.1.3 on 2024-12-06 16:53

import moviecasuals.director.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0002_director_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='first_name',
            field=models.CharField(max_length=50, validators=[moviecasuals.director.validators.CapitalLetterValidator()]),
        ),
        migrations.AlterField(
            model_name='director',
            name='last_name',
            field=models.CharField(max_length=50, validators=[moviecasuals.director.validators.CapitalLetterValidator()]),
        ),
    ]
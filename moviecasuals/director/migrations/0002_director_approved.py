# Generated by Django 5.1.3 on 2024-12-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]

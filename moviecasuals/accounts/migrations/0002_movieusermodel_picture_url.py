# Generated by Django 5.1.3 on 2024-12-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieusermodel',
            name='picture_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwatchlist',
            name='watchedmovies',
            field=models.BooleanField(max_length=50),
        ),
    ]

# Generated by Django 4.1 on 2022-09-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

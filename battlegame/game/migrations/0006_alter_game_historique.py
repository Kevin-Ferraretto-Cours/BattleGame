# Generated by Django 4.2 on 2023-04-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_game_historique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='historique',
            field=models.JSONField(default={}),
        ),
    ]

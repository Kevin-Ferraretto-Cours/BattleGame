# Generated by Django 4.2 on 2023-04-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_game_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='historique',
            field=models.JSONField(blank=True, null=True),
        ),
    ]

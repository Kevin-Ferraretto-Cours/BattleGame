# Generated by Django 4.2 on 2023-04-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_enemy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='enemy',
            name='damage',
            field=models.IntegerField(default=50),
        ),
    ]

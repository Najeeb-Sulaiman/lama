# Generated by Django 5.0.6 on 2024-08-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_teamlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='game_week',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teammetric',
            name='game_week',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teammetric',
            name='offside',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teammetric',
            name='penalty_converted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teammetric',
            name='penalty_played',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

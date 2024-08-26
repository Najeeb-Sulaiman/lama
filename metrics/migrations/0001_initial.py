# Generated by Django 5.0.6 on 2024-07-14 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('home_or_away', models.CharField(choices=[('Home', 'Home'), ('Away', 'Away'), ('Neutral', 'Neutral')], default='Home', max_length=100)),
                ('competition', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='metrics.competition')),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.team')),
            ],
        ),
        migrations.CreateModel(
            name='PhysiologicalMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.FloatField()),
                ('fatigue_level', models.IntegerField()),
                ('injury_risk', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.player')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_covered', models.FloatField()),
                ('sprints', models.IntegerField()),
                ('top_speed', models.FloatField()),
                ('acceleration', models.FloatField()),
                ('deceleration', models.FloatField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerImpactMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_influence', models.FloatField()),
                ('game_rating', models.FloatField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.position'),
        ),
        migrations.CreateModel(
            name='PsychologicalMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stress_levels', models.FloatField()),
                ('focus_and_concentration', models.FloatField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.player')),
            ],
        ),
        migrations.CreateModel(
            name='TacticalMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positioning', models.TextField()),
                ('passing_accuracy', models.FloatField()),
                ('dribbles_completed', models.IntegerField()),
                ('touches', models.IntegerField()),
                ('defensive_actions', models.IntegerField()),
                ('offensive_actions', models.IntegerField()),
                ('duels_won', models.IntegerField()),
                ('interceptions', models.IntegerField()),
                ('clearances', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.player')),
            ],
        ),
        migrations.CreateModel(
            name='TeamCohesionMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passing_networks', models.TextField()),
                ('spacing_and_movement', models.TextField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possession_percentage', models.FloatField()),
                ('goals_scored', models.IntegerField()),
                ('expected_goals', models.FloatField()),
                ('goal_assist', models.FloatField()),
                ('shots_taken', models.IntegerField()),
                ('shots_on_target', models.IntegerField()),
                ('chances_created', models.IntegerField()),
                ('conner_kicks_played', models.IntegerField()),
                ('conner_kicks_converted', models.IntegerField()),
                ('free_kicks_played', models.IntegerField()),
                ('free_kicks_converted', models.IntegerField()),
                ('goals_conceded', models.IntegerField()),
                ('expected_goals_against', models.FloatField()),
                ('tackles_won', models.IntegerField()),
                ('fouls_commited', models.IntegerField()),
                ('yellow_card', models.IntegerField()),
                ('red_card', models.IntegerField()),
                ('interceptions', models.IntegerField()),
                ('clearances', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.team')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shots_on_target', models.IntegerField()),
                ('goals_scored', models.IntegerField()),
                ('goal_assist', models.FloatField()),
                ('shots_taken', models.IntegerField()),
                ('conner_kicks_played', models.IntegerField()),
                ('conner_kicks_converted', models.IntegerField()),
                ('free_kicks_played', models.IntegerField()),
                ('free_kicks_converted', models.IntegerField()),
                ('fouls_commited', models.IntegerField()),
                ('yellow_card', models.IntegerField()),
                ('red_card', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.player')),
            ],
        ),
    ]

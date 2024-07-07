# metrics/models.py
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Match(models.Model):
    date = models.DateField()
    opponent = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class PhysicalMetric(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    distance_covered = models.FloatField()
    sprints = models.IntegerField()
    top_speed = models.FloatField()
    acceleration = models.FloatField()
    deceleration = models.FloatField()

class TechnicalMetric(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    passing_accuracy = models.FloatField()
    shots_on_target = models.IntegerField()
    dribbles_completed = models.IntegerField()
    touches = models.IntegerField()

class TacticalMetric(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    positioning = models.TextField()
    defensive_actions = models.IntegerField()
    offensive_actions = models.IntegerField()
    duels_won = models.IntegerField()

class PhysiologicalMetric(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    heart_rate = models.FloatField()
    fatigue_level = models.IntegerField()
    injury_risk = models.IntegerField()

class TeamMetric(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    possession_percentage = models.FloatField()
    goals_scored = models.IntegerField()
    expected_goals = models.FloatField()
    shots_taken = models.IntegerField()
    chances_created = models.IntegerField()
    goals_conceded = models.IntegerField()
    expected_goals_against = models.FloatField()
    tackles = models.IntegerField()
    interceptions = models.IntegerField()
    clearances = models.IntegerField()

class PlayerImpactMetric(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player_influence = models.FloatField()
    game_rating = models.FloatField()

class TeamCohesionMetric(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    passing_networks = models.TextField()
    spacing_and_movement = models.TextField()

class PsychologicalMetric(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    stress_levels = models.FloatField()
    focus_and_concentration = models.FloatField()
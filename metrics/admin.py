from django.contrib import admin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Team, TeamAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'position')
admin.site.register(Position, PositionAdmin)

class Playerdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'team')
admin.site.register(Player, Playerdmin)

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Competition, CompetitionAdmin)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'opponent')
admin.site.register(Match, MatchAdmin)

class PhysicalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'distance_covered','sprints','top_speed','acceleration','deceleration')
admin.site.register(PhysicalMetric, PhysicalMetricAdmin)

class TechnicalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'passing_accuracy','shots_on_target','dribbles_completed','touches')
admin.site.register(TechnicalMetric, TechnicalMetricAdmin)

class TacticalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'positioning','defensive_actions','offensive_actions','duels_won')
admin.site.register(TacticalMetric, TacticalMetricAdmin)

class PhysiologicalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'heart_rate','fatigue_level','injury_risk')
admin.site.register(PhysiologicalMetric, PhysiologicalMetricAdmin)

class TeamMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'match', 'possession_percentage','goals_scored','expected_goals','shots_taken','chances_created','goals_conceded','expected_goals_against','tackles','interceptions','clearances')
admin.site.register(TeamMetric, TeamMetricAdmin)

class PlayerImpactMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'player_influence','game_rating')
admin.site.register(PlayerImpactMetric, PlayerImpactMetricAdmin)

class TeamCohesionMetriccAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'match', 'passing_networks','spacing_and_movement')
admin.site.register(TeamCohesionMetric, TeamCohesionMetriccAdmin)

class PsychologicalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'stress_levels','focus_and_concentration')
admin.site.register(PsychologicalMetric, PsychologicalMetricAdmin)
#admin.site.register([Team,Player,Match,PhysicalMetric,TechnicalMetric,TacticalMetric,PhysiologicalMetric,TeamMetric,PlayerImpactMetric,TeamCohesionMetric,PsychologicalMetric], TeamAdmin)

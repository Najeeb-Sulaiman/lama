from django.contrib import admin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Team, TeamAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'position')
admin.site.register(Position, PositionAdmin)

class Playerdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')
admin.site.register(Player, Playerdmin)

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'season')
admin.site.register(Competition, CompetitionAdmin)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'competition', 'season', 'opponent', 'home_or_away')
admin.site.register(Match, MatchAdmin)

class PhysicalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'distance_covered','sprints','top_speed','acceleration','deceleration')
admin.site.register(PhysicalMetric, PhysicalMetricAdmin)

class TechnicalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'shots_on_target','goals_scored','goal_assist', 'shots_taken','conner_kicks_played','conner_kicks_converted','free_kicks_played','free_kicks_converted', 'fouls_commited', 'yellow_card','red_card')
admin.site.register(TechnicalMetric, TechnicalMetricAdmin)

class TacticalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'positioning', 'passing_accuracy', 'dribbles_completed', 'touches', 'defensive_actions','offensive_actions','duels_won', 'interceptions', 'clearances')
admin.site.register(TacticalMetric, TacticalMetricAdmin)

class PhysiologicalMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'match', 'heart_rate','fatigue_level','injury_risk')
admin.site.register(PhysiologicalMetric, PhysiologicalMetricAdmin)

class TeamMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'match', 'game_week', 'possession_percentage','goals_scored','expected_goals', 'goal_assist', 'shots_taken', 'shots_on_target','chances_created', 'conner_kicks_played', 'conner_kicks_converted', 'free_kicks_played', 'free_kicks_converted','goals_conceded','expected_goals_against','tackles_won', 'fouls_commited', 'yellow_card', 'red_card','interceptions','clearances')
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

class TeamListAdmin(admin.ModelAdmin):
    list_display = ('id', 'season', 'game_week', 'match', 'player', 'start_or_sub','minutes_played', 'position_played')
admin.site.register(TeamList, TeamListAdmin)
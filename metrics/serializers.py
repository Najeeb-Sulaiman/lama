# metrics/serializers.py
from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PhysicalMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalMetric
        fields = '__all__'

class TechnicalMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalMetric
        fields = '__all__'

class TacticalMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = TacticalMetric
        fields = '__all__'

class PhysiologicalMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysiologicalMetric
        fields = '__all__'

class TeamMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMetric
        fields = '__all__'

class PlayerImpactMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerImpactMetric
        fields = '__all__'

class TeamCohesionMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCohesionMetric
        fields = '__all__'

class PsychologicalMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologicalMetric
        fields = '__all__'

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamList
        fields = '__all__'
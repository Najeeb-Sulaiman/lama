# metrics/forms.py
from django import forms
from .models import *

class PhysicalMetricForm(forms.ModelForm):
    class Meta:
        model = PhysicalMetric
        fields = '__all__'

class TechnicalMetricForm(forms.ModelForm):
    class Meta:
        model = TechnicalMetric
        fields = '__all__'

class TacticalMetricForm(forms.ModelForm):
    class Meta:
        model = TacticalMetric
        fields = '__all__'

class PhysiologicalMetricForm(forms.ModelForm):
    class Meta:
        model = PhysiologicalMetric
        fields = '__all__'

class TeamMetricForm(forms.ModelForm):
    class Meta:
        model = TeamMetric
        fields = '__all__'

class PlayerImpactMetricForm(forms.ModelForm):
    class Meta:
        model = PlayerImpactMetric
        fields = '__all__'

class TeamCohesionMetricForm(forms.ModelForm):
    class Meta:
        model = TeamCohesionMetric
        fields = '__all__'

class PsychologicalMetricForm(forms.ModelForm):
    class Meta:
        model = PsychologicalMetric
        fields = '__all__'
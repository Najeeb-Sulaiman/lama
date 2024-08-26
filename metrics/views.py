#from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render, redirect
from .forms import *

#This part is for form
def collect_physical_metrics(request):
    if request.method == 'POST':
        form = PhysicalMetricForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PhysicalMetricForm()
    return render(request, 'metrics.html', {'form': form})

# Repeat similar views for other forms...


#This part is for API 
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class PhysicalMetricViewSet(viewsets.ModelViewSet):
    queryset = PhysicalMetric.objects.all()
    serializer_class = PhysicalMetricSerializer

class TechnicalMetricViewSet(viewsets.ModelViewSet):
    queryset = TechnicalMetric.objects.all()
    serializer_class = TechnicalMetricSerializer

class TacticalMetricViewSet(viewsets.ModelViewSet):
    queryset = TacticalMetric.objects.all()
    serializer_class = TacticalMetricSerializer

class PhysiologicalMetricViewSet(viewsets.ModelViewSet):
    queryset = PhysiologicalMetric.objects.all()
    serializer_class = PhysiologicalMetricSerializer

class TeamMetricViewSet(viewsets.ModelViewSet):
    queryset = TeamMetric.objects.all()
    serializer_class = TeamMetricSerializer

class PlayerImpactMetricViewSet(viewsets.ModelViewSet):
    queryset = PlayerImpactMetric.objects.all()
    serializer_class = PlayerImpactMetricSerializer

class TeamCohesionMetricViewSet(viewsets.ModelViewSet):
    queryset = TeamCohesionMetric.objects.all()
    serializer_class = TeamCohesionMetricSerializer

class PsychologicalMetricViewSet(viewsets.ModelViewSet):
    queryset = PsychologicalMetric.objects.all()
    serializer_class = PsychologicalMetricSerializer

class TeamListViewSet(viewsets.ModelViewSet):
    queryset = TeamList.objects.all()
    serializer_class = TeamListSerializer
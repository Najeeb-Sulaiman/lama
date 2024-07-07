# metrics/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'physical-metrics', PhysicalMetricViewSet)
router.register(r'technical-metrics', TechnicalMetricViewSet)
router.register(r'tactical-metrics', TacticalMetricViewSet)
router.register(r'physiological-metrics', PhysiologicalMetricViewSet)
router.register(r'team-metrics', TeamMetricViewSet)
router.register(r'player-impact-metrics', PlayerImpactMetricViewSet)
router.register(r'team-cohesion-metrics', TeamCohesionMetricViewSet)
router.register(r'psychological-metrics', PsychologicalMetricViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', collect_physical_metrics, name='collect_physical_metrics'),
]
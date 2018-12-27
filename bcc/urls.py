from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='bcc-home'),
    path('about/',views.about, name='bcc-about'),
    path('teams/',views.teams, name='bcc-teams'),
    path('teams/<slug:t_id>/players', views.teams, name='team-players'),
    path('teams/<slug:t_id>/schedule', views.team_schedule, name='team-schedule'),
    path('teams/<slug:t_id>/results', views.team_results, name='team-results'),
    path('teams/<slug:t_id>/stats', views.team_stats, name='team-stats'),

    path('pointsTable/',views.pointsTable, name='bcc-pointsTable'),
    path('schedule/',views.schedule, name='bcc-schedule'),
    path('stats/',views.stats, name='bcc-stats'),
    path('stats/<slug:stats_type>',views.stats, name='bcc-stats'),
    # path('teams/detail/',views.teams_detail, name='teams-detail'),

    # path('registration/',views.registration, name='bcc-registration'),
    
]
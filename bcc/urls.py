from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='bcc-home'),
    path('about/',views.about, name='bcc-about'),
    path('teams/',views.teams, name='bcc-teams'),
    path('teams/<slug:t_id>/', views.teams, name='bcc-teams-with-team_id'),
    path('pointsTable/',views.pointsTable, name='bcc-pointsTable'),
    path('schedule/',views.schedule, name='bcc-schedule'),
    path('stats/',views.stats, name='bcc-stats'),
    # path('teams/detail/',views.teams_detail, name='teams-detail'),

    # path('registration/',views.registration, name='bcc-registration'),
    
]
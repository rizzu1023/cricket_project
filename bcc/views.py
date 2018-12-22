from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    return render(request, 'bcc/home.html')

def about(request):
    return render(request, 'bcc/about.html')


def pointsTable(request):
    team = {
        'points' : points_table.objects.all().order_by('-pts','-nrr')
    }
    return render(request, 'bcc/pointsTable.html', team)
    
    
def teams(request):
    team_details = {
        'team_name' : Team.objects.all()
    }
    return render(request, 'bcc/teams.html', team_details)


def schedule(request):
    schedule_details = {
        'matches' : schedule_2019.objects.all()
    }
    return render(request,'bcc/schedule.html', schedule_details)

def stats(request):
    return render(request, 'bcc/stats.html')

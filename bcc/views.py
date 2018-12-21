from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, 'bcc/home.html')

def about(request):
    return render(request, 'bcc/about.html')


def pointsTable(request):
    team = {
        'points' : points_table.objects.all()
    }
    return render(request, 'bcc/pointsTable.html', team)
    
    
def teams(request):
    team_details = {
        'team_name' : Team.objects.all()
    }
    return render(request, 'bcc/teams.html', team_details)

from django.shortcuts import render
from .models import Team
# Create your views here.


def home(request):
    return render(request, 'bcc/home.html')

def about(request):
    return render(request, 'bcc/about.html')

def teams(request):
    team_details = {
        'team_name' : Team.objects.all()
    }
    return render(request, 'bcc/teams.html', team_details)

def pointsTable(request):
    return render(request, 'bcc/pointsTable.html')
    
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
    
    
def teams(request, t_id="default_Team"):
    if t_id=="default_Team":
        context = {
            'team_details' : Team.objects.all(),
        }
        return render(request, 'bcc/teams.html', context)
    else:
        context = {
            'p_team_detail': Team.objects.all().filter(team_id=t_id),
            'team_player': player_info.objects.filter(team_id__team_id=t_id),
        }
        return render(request, 'bcc/teamsDetail.html',context)



def schedule(request):
    schedule_details = {
        'matches' : schedule_2019.objects.all()
    }
    return render(request,'bcc/schedule.html', schedule_details)

def stats(request):
    return render(request, 'bcc/stats.html')


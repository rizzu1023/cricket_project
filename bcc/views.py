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
        if(len(Team.objects.all().filter(team_id=t_id))==0):
            return render(request, 'bcc/home.html')
        else:
            return render(request, 'bcc/teams_players.html',context)





def team_schedule(request, t_id="default_Team"):
    if t_id=="default_Team":
        return render(request, 'bcc/home.html')
    else:
        context = {
            'p_team_detail': Team.objects.all().filter(team_id=t_id),
            # 'team_player': player_info.objects.filter(team_id__team_id=t_id),
            't_schedule1' : schedule_2019.objects.filter(team_1__team_id=t_id),
            't_schedule2' : schedule_2019.objects.filter(team_2__team_id=t_id),

        }
        return render(request, 'bcc/team_schedule.html',context)
   



def team_results(request, t_id="default_Team"):
    if t_id=="default_Team":
        return render(request, 'bcc/home.html')
    else:
        context = {
            'p_team_detail': Team.objects.all().filter(team_id=t_id),
            'team_player': player_info.objects.filter(team_id__team_id=t_id),
        }
        return render(request, 'bcc/team_results.html', context)




def team_stats(request, t_id="default_Team"):
    # player_id='RH45'
    if t_id=="default_Team":
        return render(request, 'bcc/home.html')
    else:
        context = {
            'p_team_detail': Team.objects.all().filter(team_id=t_id),
            'team_player': player_info.objects.filter(team_id__team_id=t_id),
            'team_stats_batting' : batting.objects.filter(player_id__team_id__team_id=t_id).order_by('-Bt_runs'),
            'team_stats_bowling' : bowling.objects.filter(player_id__team_id__team_id=t_id).order_by('-Bw_wickets'),

        }
        return render(request, 'bcc/team_stats.html', context)






def schedule(request):
    schedule_details = {
        'matches' : schedule_2019.objects.all()
    }
    return render(request,'bcc/schedule.html', schedule_details)

def stats(request):
    return render(request, 'bcc/stats.html')


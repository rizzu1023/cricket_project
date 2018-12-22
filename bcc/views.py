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
    return render(request,'bcc/schedule.html')


# def registration(request):
#     if request.method == 'POST':
#         form = registration_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('bcc-home')
#     else:
#         form = registration_form()
#     return render(request, 'bcc/registration.html', {'form':form})
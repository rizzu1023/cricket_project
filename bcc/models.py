from django.db import models

# Create your models here.


class Team(models.Model):
    team_id = models.CharField(max_length=10)
    team_name = models.CharField(max_length=40)
    winner = models.IntegerField()
    group_name = models.CharField(max_length=10)

    def __str__(self):
        return self.team_id


class points_table(models.Model):
    team_id = models.OneToOneField(Team, on_delete='CASCADE', primary_key='True')
    matches = models.IntegerField()
    won = models.IntegerField()
    lost = models.IntegerField()
    draw = models.IntegerField()
    pts = models.IntegerField()
    nrr = models.IntegerField()

    def __str__(self):
        return self.team_id.team_name


class schedule_2019(models.Model):
    match_id = models.IntegerField(primary_key='True')
    
    team_1 = models.ForeignKey(Team, related_name='team1toteam', on_delete='models.CASCADE')
    team_2 = models.ForeignKey(Team, related_name='team2toteam', on_delete='models.CASCADE')

    tournament = models.CharField(max_length=40, default="Balapeer Cricket Tournament 2019")
    dates = models.DateField()
    times = models.TimeField()

    def __str__(self):
        return f"{self.team_1.team_name +' vs '+ self.team_2.team_name}"


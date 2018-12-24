from django.db import models
from django.db.models.signals import post_save
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


class player_info(models.Model):
    BT = 'Batsman'
    BW = 'Bowler'
    WK = 'WicketKeeper'
    AR = 'AllRounder'
    PLAYER_ROLES = (
        (BT, "BATSMAN"),
        (BW, "BOWLER"),
        (WK, "WICKET-KEEPER"),
        (AR, "ALL-ROUNDER")
    )
    player_id = models.CharField(primary_key="True", max_length=10)
    player_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    player_fname = models.CharField(max_length=50)
    player_lname = models.CharField(max_length=50)
    player_F_name = models.CharField(max_length=50, default="XYZ")
    bowling_style = models.CharField(max_length=50, default="Right Handed Batsman")
    batting_style = models.CharField(max_length=50, default="Right-arm-fast-medium")
    team_id = models.ForeignKey(Team, null="True", on_delete='models.CASCADE')
    player_role = models.CharField(max_length=30, choices=PLAYER_ROLES, default=BT)

    def __str__(self):
        return f"{self.player_id + ' ' + self.player_fname + ' ' + self.player_lname}" 



class batting(models.Model):
    player_id = models.OneToOneField(player_info, on_delete='models.CASCADE')
    Bt_matches = models.IntegerField(default=0)
    Bt_runs = models.IntegerField(default=0)
    Bt_balls = models.IntegerField(default=0)
    Bt_innings = models.IntegerField(default=0)
    Bt_fours = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.player_id)
        # return self.player_id

class bowling(models.Model):
    player_id = models.OneToOneField(player_info, on_delete='models.CASCADE')
    Bw_runs = models.IntegerField(default=0)
    Bw_balls = models.IntegerField(default=0)
    Bw_innings = models.IntegerField(default=0)
    Bt_wicket = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.player_id)


def create_player_objects(sender, **kwargs):
    if kwargs['created']:
        player_batting = batting.objects.create(player_id=kwargs['instance'])
        player_bowling = bowling.objects.create(player_id=kwargs['instance'])

post_save.connect(create_player_objects, sender=player_info)
from django.db import models

# Create your models here.
class Test(models.Model):
    user_id = models.IntegerField()
    password = models.CharField(max_length=20)   #length parameter is compulsory

    def __str__(self):
        return self.password          #can't return a integer value


class Team(models.Model):
    team_id = models.CharField(max_length=10)
    team_name = models.CharField(max_length=40)
    winner = models.IntegerField()
    group_name = models.CharField(max_length=10)

    def __str__(self):
        return self.team_name


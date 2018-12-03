from django.db import models

# Create your models here.
class Test(models.Model):
    user_id = models.IntegerField()
    password = models.CharField(max_length=20)   #length parameter is compulsory

    def __str__(self):
        return self.password          #can't return a integer value



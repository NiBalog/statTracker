
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    userNameText = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    def __str__(self):
        return self.userNameText

class gameStats(models.Model):
    Rank = models.CharField(max_length=250)

    Map = models.CharField(max_length=250)

    ScoreAtHalf = models.CharField(max_length=250)

    FinalScore = models.CharField(max_length=250)

    Kills = models.IntegerField(default=0)

    Deaths = models.IntegerField(default=0)

    Assists = models.IntegerField(default=0)


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

class Results(models.Model):
    game = models.CharField(max_length=250, default = 'game title')
    kills = models.IntegerField()
    deaths = models.IntegerField()
    time = datetime.datetime.now()

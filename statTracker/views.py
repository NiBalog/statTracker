from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def homePage(request):
    return HttpResponse("This is the home page where you can go to the different places on the site")

def statPage(request, question_id):
    return HttpResponse("You're Looking at your own stats")

def addStats(request, question_id):
    return HttpResponse("You are adding stats to your file")

def otherUsersStats(request, question_id):
    return HttpResponse("You are looking at %s's stats" % username)

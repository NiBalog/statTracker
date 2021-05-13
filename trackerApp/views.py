
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.utils import timezone
from .models import Profile, Results
from django.contrib.auth.models import User

# Create your views here.

class WelcomeView(View):
    def get(self,request):
        template_name = "trackerApp/welcomePage.html"
        return render(request, template_name)
class HomePageView(View):
    def get(self,request):
        template_name = "trackerApp/SiegeHomeView.html"
        return render(request, template_name)

class ProfileView(View):
    def get(self,request):
        template_name = "trackerApp/addStats.html"
        userNameText = Profile.objects.all();
        context = {
            'userNameText':userNameText
            }
        return render(request, template_name, context)

    def post(self,request):
        if request.POST:
            addStats = Results(
                game = request.POST['game'],
                kills = request.POST['kills'],
                deaths = request.POST['deaths']
            )

            addStats.save()

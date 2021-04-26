
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.utils import timezone
from .models import Profile, gameStats

# Create your views here.
class ProfileView(View):
    def get(self,request):
        template_name = "trackerApp/addStats.html"
        userNameText = Profile.objects.all();
        context = {
            'userNameText':userNameText
            }
        return render(request, template_name, context)

class index(request):
    if request.POST:
        

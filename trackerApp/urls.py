from django.urls import path

from . import views

app_name = 'trackerApp'
urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcomePage');
    path('',views.HomePageView.as_view(), name = 'homePage');
]

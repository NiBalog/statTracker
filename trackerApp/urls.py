from django.urls import path

from . import views

app_name = 'trackerApp'
urlpatterns = [
    path('', views.ProfileView.as_view(), name='index')
]

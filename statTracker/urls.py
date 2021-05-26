
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('trackerApp.urls')),
    path('trackerApp/', include('trackerApp.urls', namespace = 'tracker')),
    path('admin/', admin.site.urls),
]

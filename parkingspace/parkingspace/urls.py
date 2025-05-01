# parkingspace/urls.py

from django.contrib import admin
from django.urls import path
from . import views  
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parking_video/', views.parking_video, name='parking_video'),
    path('parking_video_2/', views.parking_video_2, name='parking_video_2'),  # Burada adın doğru olduğuna dikkat edin
    path('', views.home, name='home'),
]

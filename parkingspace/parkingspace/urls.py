# parkingspace/urls.py

from django.contrib import admin
from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parking_video/', views.parking_video, name='parking_video'),
    path('parking_video_2/', views.parking_video_2, name='parking_video_2'),  # Burada adın doğru olduğuna dikkat edin
    path('Ebebek/', views.Ebebek, name='Ebebek'),
    path('AkasyaAWM/', views.AkasyaAWM, name='AkasyaAWM'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
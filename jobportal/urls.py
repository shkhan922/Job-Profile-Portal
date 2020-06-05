from django.contrib import admin
from django.conf import settings 
from django.urls import path
from django.conf.urls.static import static

from .views import index, jobsector, jobprofile, login , register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('jobsector/', jobsector),
    path('jobprofile/', jobprofile),
    path('login/', login),
    path('register/', register),
    
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.conf import settings 
from django.urls import path
from django.conf.urls.static import static

from . import views

from .views import index, jobsector_list, jobprofile, loginPage , register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
   # path('jobsector_list/<str:job_cat>/', views.jobsector_list, name="jobsector_list"),
    path('jobsector_list/<str:slug>/', views.jobsector_list, name="jobsector_list"),
    path('jobprofile/', jobprofile),
    path('login/', loginPage),
    path('register/', register),
    
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

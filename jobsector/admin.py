from django.contrib import admin

from .models import Jobsector, Jobcategory

admin.site.register(Jobsector)
admin.site.register(Jobcategory)
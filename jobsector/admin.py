from django.contrib import admin

from .models import Jobsector, Jobcategory, Jobprofile

admin.site.register(Jobsector)
admin.site.register(Jobcategory)
admin.site.register(Jobprofile)
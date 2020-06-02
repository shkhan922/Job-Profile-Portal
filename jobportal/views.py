from django.shortcuts import render
from jobsector.models import Jobsector

def index(request):
    queryset = Jobsector.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)

def jobsector(request):
    queryset = Jobsector.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'jobsector.html', context)

def jobprofile(request):
    return render(request, 'jobprofile.html', {})

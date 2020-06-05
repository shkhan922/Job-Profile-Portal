from django.shortcuts import render
from jobsector.models import Jobsector
from jobprofile.models import Jobprofile

def index(request):
    queryset = Jobsector.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def jobsector(request):
    queryset = Jobprofile.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'jobsector.html', context)

def jobprofile(request):
    queryset = Jobprofile.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'jobprofile.html', context)
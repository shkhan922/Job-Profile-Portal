from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def jobsector(request):
    return render(request, 'jobsector.html', {})

def jobprofile(request):
    return render(request, 'jobprofile.html', {})

from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def jobsector(request):
    def jobsector(request):
    queryset = Jobsector.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'jobsector.html', context)

def jobprofile(request):
    queryset = jobprofile.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'jobprofile.html', context)

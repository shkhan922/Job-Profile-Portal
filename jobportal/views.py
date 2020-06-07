from django.shortcuts import render, redirect
from jobsector.models import Jobsector
from jobprofile.models import Jobprofile
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
 
from django.contrib import messages

from .forms import CreateUserForm


def index(request):
    queryset = Jobsector.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    context = {}
    return render(request, 'login.html', {})


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for  ' + user)
            return redirect(loginPage)
             
    context = {'form': form}
    return render(request, 'register.html', context)


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

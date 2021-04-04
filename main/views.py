from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic.dates import *
from .forms import *


def index(request):
    user = request.user
    context = {'user': user}
    return render(request, 'index.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    context = {}
    return render(request, 'login.html', context)

class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST or None)
        context = {'form': form}
        return render(request, 'register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            # login(request, user)
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form, }
        return render(request, 'register.html', context)

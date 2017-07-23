from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from .forms import *
from .models import *

# Create your views here.


def index(request):
    return render(request,'farmdb/test.html')

def create_farmer(request):
    form = Create_Farmer_Form(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("<html><body><h1>Welcome, {}</h1></body></html>".format(user.first_name))
                #Do what needs to be done after a user logs in
    context = {
        "form": form,
    }
    return render(request, 'farmdb/register.html', context)

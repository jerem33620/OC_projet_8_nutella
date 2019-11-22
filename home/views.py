from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from .forms import ConnexionForm, SignUpForm
import requests


def home(request):
    return render(request, 'home.html')

def login(request):
    """Pour pouvoir se connecter"""
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                auth.login(request, user)
                context = {
                    "user": request.user,
                }
                return redirect("home")
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    context = {"form":form}

    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect("home")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
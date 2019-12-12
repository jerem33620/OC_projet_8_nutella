from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from home.forms import ConnexionForm, SearchForm, SingupForm
from .models import User

def login(request):
    """ Cette fonction sert à se connecter sur le site """
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
    """ Cette méthode sert à se déconnecter """
    auth.logout(request)
    return redirect("home")

def signup(request):
    """ Cette méthode sert à s'enregistrer """
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username, email=email, password=raw_password)
            login(request, user)
            user.save()
            return redirect('home')
    else:
        form = SingupForm()
    return render(request, 'signup.html', {'form': form}) 
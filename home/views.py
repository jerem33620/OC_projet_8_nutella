from django.shortcuts import render
from django.contrib.auth import login

from .forms import SearchForm


def home(request):
    form = SearchForm()
    return render(request, 'home.html', {"form":form})

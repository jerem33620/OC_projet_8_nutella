from django.shortcuts import render


def home(request):
    form = SearchForm()
    return render(request, 'home.html', {"form":form})

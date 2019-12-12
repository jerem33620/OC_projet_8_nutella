from django.shortcuts import render

from home.forms import SearchForm
from .models import Product, Category


def research(request):
    """ Cette méthode sert à créer la requête en GET pour obtenir des substitues """
    substitute = []
    if request.method == "GET":
        form = SearchForm(request.GET or None)
        if form.is_valid():
            substitutes = Product.objects.find_products(form)
    return render(request, "research.html", {"substitutes": substitutes})
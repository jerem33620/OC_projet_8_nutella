from django.shortcuts import render

from home.forms import SearchForm
from .models import Product, Category


def research(request):
    substitute = []
    if request.method == "GET":
        form = SearchForm(request.GET or None)
        if form.is_valid():
            substitutes = Product.objects.find_substitutes(form)
    return render(request, "research.html", {"substitutes": substitutes})
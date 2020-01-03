from django.db import models
from django.conf import settings


class ProductManager(models.Manager):
    """ Cette class sert à appelé les produits lors de la recherche sur le site """
    def find_products(self, form):
        from .models import Product

        substitutes = []
        product = None
        searched_name = form.cleaned_data["product"]
        products = Product.objects.filter(product_name__icontains=searched_name)
        if products:
            product = products[0]
            substitutes = list(
                Product.objects.filter(
                    category=product.category, 
                    nutrition_grade_fr__lt=product.nutrition_grade_fr,
                )[:settings.MAX_RESULT]
            )
        return substitutes, product

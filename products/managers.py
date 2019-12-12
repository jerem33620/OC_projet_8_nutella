from django.db import models


class ProductManager(models.Manager):
    def find_substitutes(self, form):
        from .models import Product

        substitutes = []
        searched_name = form.cleaned_data["product"]
        products = Product.objects.filter(product_name__icontains=searched_name)
        if products:
            product = products[0]
            category = product.category
            nutrition_grade_fr = product.nutrition_grade_fr
            substitutes = list(
                Product.objects.filter(
                    category=product.category, 
                    nutrition_grade_fr__lt=product.nutrition_grade_fr
                )
            )
        return substitutes

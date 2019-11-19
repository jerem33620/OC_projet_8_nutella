from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests

from products.models import Category, Product
from openfoodfacts.utils import get_json


class Command(BaseCommand):
    help = (
        "Downloads products from openfoodfacts and saves products in database"
    )

    def handle(self, *args, **options):
        self.codes=set()
        self.delete_all()
        for category in settings.OPENFOODFACTS_CATEGORIES:
            category, created = self.save_category(
                category
            )  # 0. Sauvegarder la catégories dans le modèle Category
            
            products = get_json(
                category.name
            )  # 1. downloader les produits pour chaque catégorie
            
            products = self.clean_products(
                products
            )  # 2. Eliminer les produits pour lesquels il manque des infos
            
            self.save_products_by_category(
                category, products
            )  # 3. Sauvegarder les produits dans la base

    def save_category(self, category):
        return Category.objects.get_or_create(name=category.lower())

    def save_products_by_category(self, category, products):
        for product in products:
            self.stdout.write(str(product["product_name"]))
            if product["code"] not in self.codes:
                self.codes.add(product["code"])
                Product.objects.get_or_create(
                    code=product["code"],
                    product_name=product["product_name"],
                    category=category,
                    nutrition_grade_fr=product["nutrition_grade_fr"],
                    url=product["url"],
                    image_url=product["image_url"],
                    image_nutrition_url=product["image_nutrition_url"],
                )

    def _is_valid(self, product):
        """Vérifier que toutes les infos nécessaires sont présentes dans le 
        dictionnaire product."""
        keys = ("code", "product_name", "nutrition_grade_fr",
                "url", "image_url", "image_nutrition_url")
        for key in keys:
            if key not in product or not product[key]:
                return False
        return True

    def clean_products(self, products):
        cleaned_products = []

        for product in products:
            if self._is_valid(product):
                cleaned_products.append(product)

        return cleaned_products

    def delete_all(self):
        Product.objects.all().delete()
        Category.objects.all().delete()
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Product(models.Model):
    code = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    nutrition_grade_fr = models.CharField(max_length=3)
    url = models.URLField(max_length=255)
    image_url = models.URLField(max_length=255)
    image_nutrition_url = models.URLField(max_length=255)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )

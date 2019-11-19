from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product
from django.conf import settings


class User(AbstractUser):
    pass

class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="favorites_as_product"
    )
    substitute = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="favorites_as_substitute"
    )

#class Profile(models.Model):
#    user = models.OneToOneField('auth.User', on_delete=models.cascade)
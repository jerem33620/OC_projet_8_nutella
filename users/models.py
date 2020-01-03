from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product
from django.conf import settings
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    """ Cette class sert à utiliser AbstractUser pour obtenir tous ce qu'il nous faut pour un utilisateur """
    objects = UserManager()

class Favorite(models.Model):
    """ Cette class sert à avoir une table de favoris pour enregistrer
        les utilisateurs, les produits recherchés et les substitues trouvés
    """
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
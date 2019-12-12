from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ConnexionForm(forms.Form):
    """ Cette class sert à pouvoir utiliser l'username et le password pour se connecter """
    username = forms.CharField(label="Nom d'utilisateur", max_length=20)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, min_length=6, max_length=16)

class SearchForm(forms.Form):
    """ Cette class sert à montré le champd de recherche sur le site pour trouvé le produit demandé """
    product = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': "Champs de recherche"})
)

class SingupForm(UserCreationForm):
    """ Cette class sert à enregistrer username, ces 2 password et l'email """
    email = forms.CharField(label="email")

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
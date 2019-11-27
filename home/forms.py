from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=20)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, min_length=6, max_length=16)

class SearchForm(forms.Form):
    product = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': "Champ de recherche pour les produits"})
)

class SingupForm(UserCreationForm):
    email = forms.CharField(label="email")

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
from django.urls import path

from . import views


urlpatterns = [
    path('save/', views.favorite_save, name='favorite_save'),
]
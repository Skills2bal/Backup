from importlib.resources import path

from django.urls import path
from .views import *

urlpatterns = [
    path('crud/' , Crud.as_view()), # Lien qui permet de faire l CRUD
    path('getinstance/' , GetInstance.as_view()), # Lien qui renvoie la facture d'un bordereau
    path('getfactureborderau/', GetFactureBorderau.as_view()), # Lien qui renvoie les facture qui apprtient a bordeau
]
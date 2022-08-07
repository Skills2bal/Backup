from django.urls import path
from .views import *

urlpatterns = [
    path('crud/', Crud.as_view()), # Methode CRUD
    path('getinstance/', GetInstance.as_view()), #Recupere une instance
    path('getfacturebordeaux/', GetFactureBorderaux.as_view()), # Recuperer toutes les facture d'un Bureau)
         
]
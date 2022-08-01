from django.urls import path

from App.Administration.Fournisseur.views import Crud, GetInstance

urlpatterns = [
    path('crud/', Crud.as_view()),
    path('getinstance/', GetInstance.as_view())
]
from django.urls import path
from .views import *

urlpatterns = [
    path('crud/', Crud.as_view()),
    path('getinstance/', GetInstance.as_view()),
    path('depense_bureau/', GetDepenseBureau.as_view()),
]
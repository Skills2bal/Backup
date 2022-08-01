from sys import path_hooks
from django.urls import path
from .views import Crud,GetInstance


urlpatterns = [
    path('crud/', Crud.as_view()),
    path('getinstance/', GetInstance.as_view()),
]
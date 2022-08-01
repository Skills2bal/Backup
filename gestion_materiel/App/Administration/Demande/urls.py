from django.urls import path
from .views import *

urlpatterns = [
    path('crud/', Add.as_view()),
    
]
from django.urls import path
from .views import *


urlpatterns = [
    path('crud/', AddSerializer.as_view())
]

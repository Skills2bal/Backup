from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('login/', Login.as_view()),
    path('obtaintoken/', ObtainAuthToken.as_view())
]

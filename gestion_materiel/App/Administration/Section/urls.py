from importlib.resources import path
from xml.etree.ElementInclude import include
from django.urls import URLPattern

from django.urls import path
from .views import *

urlpatterns = [
    path('crud/' , Crud.as_view()),
    path('getinstance/' , GetInstance.as_view()),
    path('division_section/' ,SectionDivision.as_view())
]
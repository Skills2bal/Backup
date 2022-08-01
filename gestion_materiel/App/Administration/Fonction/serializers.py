from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from App.models import Fonction

#
class FonctionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fonction
        fields = ['fonction_libelle'] 
    
class GetFonctionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fonction
        fields = '__all__'
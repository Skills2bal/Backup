#Importation 
from rest_framework import serializers
from App.models import MaterielDemande

class AjoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterielDemande
        fields = ['demande_demande', 'materiel_demande_libelle']
        
class AjoutPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterielDemande
        fields = ['materiel_demande_libelle']
        
class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterielDemande
        fields = '__all__'

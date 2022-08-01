#Importation 
from rest_framework import serializers
from App.models import Bordereaux

class AjoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bordereaux
        fields = ['commande_commande']
                
class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bordereaux
        fields = '__all__'

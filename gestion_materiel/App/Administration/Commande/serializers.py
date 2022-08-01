from rest_framework import serializers
from App.models import Commande

class AjoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['personel_personel', 'fournisseur_fournisseur']
        
class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields ='__all__'
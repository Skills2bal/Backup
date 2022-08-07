#Importation 
from rest_framework import serializers
from App.models import Bordereaux

class BordereauxAjoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bordereaux
        fields = ['commande_commande']
                
class GetBordereauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bordereaux
        fields = '__all__'

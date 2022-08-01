from pyexpat import model
from rest_framework import serializers
from App.models import Facture

class FactureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = ['facture_copie']
        
class GetFactureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'
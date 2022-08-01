from pyexpat import model
from rest_framework import serializers
from App.models import Depense

class DepenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Depense
        fields = ['depense_libelle', 'depense_montant', 'depense_date', 'bureaux_bureaux']
    
class DepensePutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Depense
        fields = ['depense_libelle', 'depense_montant', 'depense_date' ]
        
class GetDepenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Depense
        fields = '__all__'
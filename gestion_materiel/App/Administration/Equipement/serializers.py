from rest_framework import serializers
from App.models import Equipement

class EquipementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = ['equipement_libelle', 'equipement_categorie', 'equipement_caracteristique']
        
class GetEquipementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'
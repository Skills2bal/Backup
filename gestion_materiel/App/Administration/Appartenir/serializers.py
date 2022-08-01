from pyexpat import model
from rest_framework import serializers
from App.models import  Appartenir

class AppartenirSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appartenir
        fields = ['appartenir_dte', 'bureaux_bureaux', 'materiel_dote_materiel_dote', 'appartenir_status']
        
class GetAppartenirSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appartenir 
        fields = '__all__'
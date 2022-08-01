from rest_framework import serializers
from App.models import Personel

class AddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personel
        fields = ['personel_nom',
                  'personel_prenom',
                  'personel_matricule',
                  'personel_telefone',
                  'personel_grade'
                 ]

class GetSerializerPersonnel(serializers.ModelSerializer):
    
    class Meta:
        model = Personel
        fields = [
                  'personel_id',
                  'personel_nom',
                  'personel_prenom',
                  'personel_matricule',
                  'personel_telefone',
                  'personel_grade'
                 ]
from rest_framework import serializers

from App.models import Fournisseur


class AjoutSerializer(serializers.ModelSerializer):
    class Meta:
        model= Fournisseur
        fields= ['fournisseur_nom', 'fournisseur_prenom', 'fournisseur_adresse', 'fournisseur_telefone']


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'

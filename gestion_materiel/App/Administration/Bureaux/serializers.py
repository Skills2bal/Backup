from rest_framework import serializers
from App.models import Bureaux

class BureauxSerializers(serializers.ModelSerializer):

    section_section = serializers.IntegerField()
    class Meta:
        model = Bureaux
        fields = ['section_section','bureaux_code', 'bureaux_libelle']
        
        
class BureauxPutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bureaux
        fields = ['bureaux_libelle']
        
class GetBureauxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bureaux
        fields ='__all__'

class BureauxPutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bureaux
        fields = ['bureaux_libelle']
#Importation 
#import imp
#from pyexpat import model
from rest_framework import serializers
from App.models import Section

class AjoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['division_division', 'section_code','section_libelle']
        
class GetSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

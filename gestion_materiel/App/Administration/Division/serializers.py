from rest_framework import serializers
from App.models import Division

class CrudSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = ['division_code','division_libelle']

class GetDivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = ['division_id','division_code','division_libelle']
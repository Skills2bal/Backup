from rest_framework import serializers

from App.models import Affecter

class AddAffectationSerializer(serializers.ModelSerializer):

    bureau = serializers.CharField(max_length = 100)
    personnel = serializers.CharField(max_length = 100)
    fonction = serializers.CharField(max_length = 100)

    class Meta:
        model = Affecter
        fields = ['bureau','fonction','personnel']

class GetAffectationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Affecter
        fields = ('affecter_dte',)



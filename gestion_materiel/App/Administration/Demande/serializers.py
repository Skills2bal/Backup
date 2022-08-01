from rest_framework import serializers
from App.models import *


class AddDemandeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demande
        fields = ['demande_lien']


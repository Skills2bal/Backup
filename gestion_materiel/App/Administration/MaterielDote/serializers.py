from rest_framework import serializers
from App.models import MaterielDote

class MaterielDoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaterielDote
        fields = ['materiel_dote_numero', 'materiel_dote_libelle', 'materiel_dote_categorie', 'materiel_dote_caracteristique',
                  'materiel_dote_dureevie', 'materiel_dote_taux', 'materiel_dote_status']
        
class GetMaterielDoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaterielDote
        fields = '__all__'
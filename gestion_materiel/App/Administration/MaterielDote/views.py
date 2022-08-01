from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

class Crud(APIView):
    #Ajouter
    def post(self, request):
        serial = MaterielDoteSerializers(data = request.data)
        print(serial.is_valid())
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Modifier
    def put(self, request):
        try:
            materieldote = MaterielDote.objects.get(materiel_dote_id = request.query_params.get('materiel_dote_id'))
            serial = MaterielDoteSerializers(data = request.data)
            if serial.is_valid():
                materieldote.materiel_dote_numero = serial.data['materiel_dote_numero']
                materieldote.materiel_dote_libelle = serial.data['materiel_dote_libelle']
                materieldote.materiel_dote_categorie = serial.data['materiel_dote_categorie']
                materieldote.materiel_dote_caracteristique = serial.data['materiel_dote_caracteristique']
                materieldote.materiel_dote_dureevie = serial.data['materiel_dote_dureevie']
                materieldote.materiel_dote_taux = serial.data['materiel_dote_taux']
                materieldote.materiel_dote_status = serial.data['materiel_dote_status']
                materieldote.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Supprimer
    def delete(self, request):
        try:
            materieldoter = MaterielDote.objects.get(materiel_dote_id = request.query_params.get('materiel_dote_id'))
            materieldoter.delete()
            return Response(status=status.HTTP_200_OK)
        except:
             return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Afficher tout
    def get(self, request):
        materieldote = MaterielDote.objects.all()
        serial = GetMaterielDoteSerializers(materieldote, many = True)
        return Response(status=status.HTTP_200_OK, data={'materieldote': serial.data})
        
class GetInstance(APIView):
    #get instance
    def get(self, request):
        try:
            materieldote = MaterielDote.objects.get(materiel_dote_id = request.query_params.get('materiel_dote_id'))
            serial = GetMaterielDoteSerializers(materieldote)
            return Response(status=status.HTTP_200_OK, data = {'materieldote': serial.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
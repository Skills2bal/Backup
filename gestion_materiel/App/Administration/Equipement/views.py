from os import stat
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status

#class Crud
class Crud(APIView):
    #Ajouter
    def post(self, request):
        serial = EquipementSerializers(data = request.data)
        if serial.is_valid():
            equipement = serial.save()
            serial = GetEquipementSerializers(equipement)
            return Response(status=status.HTTP_201_CREATED, data= serial.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Modifier
    def put(self, request):
        try:
            equipement = Equipement.objects.get(equipement_id = request.query_params.get('equipement_id'))
            serial = EquipementSerializers(data = request.data)
            if serial.is_valid():
                equipement.equipement_libelle = serial.data['equipement_libelle']
                equipement.equipement_categorie = serial.data['equipement_categorie']
                equipement.equipement_caracteristique = serial.data['equipement_caracteristique']
                equipement.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        
    #Supprimer
    def delete(self, request):
        try:
            equipement = Equipement.objects.get(equipement_id = request.query_params.get('equipement_id'))
            equipement.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
                
    def get(self, request):
        equipement = Equipement.objects.all()
        serial = GetEquipementSerializers(equipement, many = True)
        return Response(status=status.HTTP_200_OK, data = {'equipement': serial.data})
    
class GetInstance(APIView):
    def get(self, request):
        try: 
            equipement = Equipement.objects.get(equipement_id = request.query_params.get('equipement_id'))
            serial = GetEquipementSerializers(equipement)
            return Response(status=status.HTTP_200_OK, data={'equipement': serial.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
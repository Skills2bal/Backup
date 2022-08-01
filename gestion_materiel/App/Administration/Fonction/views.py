from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

#Class qui permet de faire le CRUD
class Crud(APIView):
    
    #Fonction Ajout
    def post(self, request):
        serial = FonctionSerializers(data = request.data)
        #print(request.data)
        #print(serial.is_valid())
        if serial.is_valid():
            fonction = serial.save()
            serial = GetFonctionSerializers(fonction)
            return Response(status = status.HTTP_200_OK, data={'fonction': serial.data})
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    #Fonction Ajout
    def put(self, request):
        try:
            fonction = Fonction.objects.get(fonction_id = request.query_params.get('fonction_id'))
            serial = FonctionSerializers(data = request.data)
            if serial.is_valid():
                fonction.fonction_libelle = serial.data['fonction_libelle']
                fonction.save()
                return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Fonction Supprimer
    def delete(self, request):
        try:
            fonction = Fonction.objects.get(fonction_id = request.query_params.get('fonction_id'))
            fonction.delete() 
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #Fonction Select all
    def get(self, request):
        fonction = Fonction.objects.all()
        serial = GetFonctionSerializers(fonction, many = True)
        return Response(status=status.HTTP_200_OK, data = {'fonction' : serial.data})
    
#class Pour recupere une instance
class GetInstance(APIView):
    def get(self, request):
        try:
            fonction = Fonction.objects.get(fonction_id = request.query_params.get('fonction_id'))
            serial = GetFonctionSerializers(fonction)
            return Response(status=status.HTTP_200_OK, data = {'fonction': serial.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
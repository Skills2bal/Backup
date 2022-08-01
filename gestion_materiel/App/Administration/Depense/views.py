from distutils import dep_util
from os import set_inheritable
from re import S
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

class Crud(APIView):
    # Ajouter
    def post(self, request):
        serial = DepenseSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # Afficher tout les elements
    def get(self, request):
        depense = Depense.objects.all()
        serial = GetDepenseSerializers(depense, many = True)
        return Response(status=status.HTTP_200_OK, data={'depense': serial.data})
    
    # Supprimer 
    def delete(self, request):
        try:
            depense = Depense.objects.get(depense_id = request.query_params.get('depense_id'))
            depense.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    # Modifier
    def put(self, request):
        try:
            depense = Depense.objects.get(depense_id = request.query_params.get('depense_id'))
            serial = DepensePutSerializers(data = request.data)
            if serial.is_valid():
                depense.depense_libelle = serial.data['depense_libelle']
                depense.depense_montant = serial.data['depense_montant']
                depense.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class GetInstance(APIView):
    # Recupere un element
    def get(self, request):
        try:
            depense = Depense.objects.get(depense_id = request.query_params.get('depense_id'))
            serial = GetDepenseSerializers(depense)
            return Response(status=status.HTTP_200_OK, data = {'depense': serial.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
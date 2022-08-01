import imp
from os import set_inheritable
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from App.models import Bordereaux
from .serializers import *

class Crud(APIView):
    def post(self, request):
        serial = FactureSerializers(data = request.data)
        if serial.is_valid():
            borderaux = Bordereaux.objects.get(bordereaux_id = request.query_params.get('bordereaux_bordereaux'))
            facture = Facture.objects.create(bordereaux_bordereaux = borderaux,
                                             facture_copie = serial.data['facture_copie'])
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        facture = Facture.objects.all()
        serial = GetFactureSerializers(facture, many = True)
        return Response(status=status.HTTP_200_OK, data={'facture': serial.data})
    
    def delete(self, request):
        try:
            facture = Facture.objects.get(facture_id = request.query_params.get('facture_id'))
            facture.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            facture = Facture.objects.get(facture_id = request.query_params.get('facture_id'))
            serial = FactureSerializers(data = request.data)
            if serial.is_valid():
                facture.facture_copie = serial.data['facture_copie']
                facture.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class GetInstance(APIView):
    def get(self, request):
        try:
            facture = Facture.objects.get(facture_id = request.query_params.get('facture_id'))
            serial = GetFactureSerializers(facture)
            return Response(status=status.HTTP_200_OK, data={'facture': serial.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
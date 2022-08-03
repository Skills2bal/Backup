
import imp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from App.models import Bureaux
from App.Administration.Bureaux.serializers import *

class Crud(APIView):
    # Ajouter
    def post(self, request):
        serial = DepenseSerializers(data = request.data)
        if serial.is_valid():
            bureau = Bureaux.objects.get(bureaux_id = serial.data['bureaux_bureaux'])
            depense = Depense.objects.create(bureaux_bureaux = bureau,
                                             depense_libelle = serial.data['depense_libelle'],
                                             depense_montant = serial.data['depense_montant'])
            serial_depense = GetDepenseSerializers(depense)
            serial_bureau = GetBureauxSerializers(depense.bureaux_bureaux)
            return Response(status=status.HTTP_201_CREATED, data={'depense': serial_depense.data, 'bureau': serial_bureau.data})
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
        
        
class GetDepenseBureau(APIView):

    def get(self,request):

        depense = Depense.objects.filter(bureaux_bureaux = request.query_params.get('bureau'))
        data = []
        for i in depense:
            data.append(
                    GetDepenseSerializers(i).data,
            )
        return Response(status=status.HTTP_200_OK, data = {'depense': data})
# Importation
from genericpath import samestat
from telnetlib import SE
from xmlrpc.client import ResponseError
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from App.Administration.Bordereau.serializers import *
from App.models import Bordereaux, Facture
from App.Administration.Commande.serializers import *


class Crud(APIView):
    def post(self, request):
        seria = BordereauxAjoutSerializer(data=request.data)
        if seria.is_valid():
            commande = Commande.objects.get(commande_id = request.query_params.get('commande_commande'))
            borderau = Bordereaux.objects.create(commande_commande = commande)
            serial_borderau = GetBordereauSerializer(borderau)
            serial_commande = GetCommandeSerializer(borderau.commande_commande)
            datas = {'commande': serial_commande.data, 'borderau': serial_borderau.data}
            return Response(status=status.HTTP_201_CREATED, data=datas)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            bordereau = Bordereaux.objects.get(bordereaux_id = request.query_params.get('bordereaux_id'))
            bordereau.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Fonction qui renvoie chaque facture avec sa commande
    def get(self, request):
        bordereau = Bordereaux.objects.all()
        data = list()
        for i in bordereau:
            data.append({
                'commande': GetCommandeSerializer(i.commande_commande).data,
                'facture': GetBordereauSerializer(i).data
            })
        return Response(status=status.HTTP_200_OK, data = {'facture': data})


class GetInstance(APIView):
    # Facture qui affiche une instance d'un borderau
    def get(self, request):
        try:
            bordereau = Bordereaux.objects.get(bordereaux_id=request.query_params.get('bordereaux_id'))
            seria = GetBordereauSerializer(bordereau)
            return Response(status=status.HTTP_200_OK, data={'Bordereau': seria.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class GetFactureBorderau(APIView):
    # Fonction qui renvoi toutes les factures qui appartient a un bureau
    def get(self, request):
        facture = Facture.objects.get(commande_commande = request.query_params.get('commande'))
        data = []
        for i in facture:
            data.append(
                GetBordereauSerializer(i).data
            )
        return Response(status=status.HTTP_200_OK, data = {'facture': data})
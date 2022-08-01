# Importation
from telnetlib import SE
from xmlrpc.client import ResponseError
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializer import *
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from App.Administration.MaterielDemander.serializers import *
from App.models import MaterielDemande


class Crud(APIView):
    def post(self, request):
        seria = AjoutSerializer(data=request.data)
        print(seria.is_valid())
        if seria.is_valid():
            seria.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            materiel_demande = MaterielDemande.objects.get(materiel_demande_id = request.query_params.get('materiel_demande_id'))
            materiel_demande.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            materiel_demande = MaterielDemande.objects.get(materiel_demande_id=request.query_params.get('materiel_demande_id'))
            seria = AjoutPutSerializer(data=request.data)
            if seria.is_valid():
                materiel_demande.materiel_demande_libelle = seria.data['materiel_demande_libelle']
                materiel_demande.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        materiel_demande = MaterielDemande.objects.all()
        seria = GetSerializer(materiel_demande, many=True)
        return Response(status=status.HTTP_200_OK, data={'materiel_demande': seria.data})


class GetInstance(APIView):
    def get(self, request):
        try:
            materiel_demande = MaterielDemande.objects.get(materiel_demande_id=request.query_params.get('materiel_demande_id'))
            seria = GetSerializer(materiel_demande)
            return Response(status=status.HTTP_200_OK, data={'materiel_demande': seria.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
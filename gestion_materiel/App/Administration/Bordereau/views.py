# Importation
from telnetlib import SE
from xmlrpc.client import ResponseError
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from App.Administration.Bordereau.serializers import *
from App.models import Bordereaux


class Crud(APIView):
    def post(self, request):
        seria = AjoutSerializer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            bordereau = Bordereaux.objects.get(bordereaux_id = request.query_params.get('bordereaux_id'))
            bordereau.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

   
    def get(self, request):
        bordereau = Bordereaux.objects.all()
        seria = GetSerializer(bordereau, many=True)
        return Response(status=status.HTTP_200_OK, data={'bordereau': seria.data})


class GetInstance(APIView):
    def get(self, request):
        try:
            bordereau = Bordereaux.objects.get(bordereaux_id=request.query_params.get('bordereaux_id'))
            seria = GetSerializer(bordereau)
            return Response(status=status.HTTP_200_OK, data={'Bordereau': seria.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
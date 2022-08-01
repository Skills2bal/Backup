from multiprocessing.pool import ApplyResult
from webbrowser import get
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

class Crud(APIView):
    def post(self, request):
        serial = AppartenirSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        apparetnir = Appartenir.objects.all()
        serial = GetAppartenirSerializers(apparetnir, many = True)
        return Response(status=status.HTTP_200_OK, data = {'appartenir': serial.data})
    
    def delete(self, request):
        try:
            appartenir = Appartenir.objects.get(id = request.query_params.get('id'))
            appartenir.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
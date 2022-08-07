from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from App.Administration.Commande.serializers import *
from App.models import Commande

class Crud(APIView):
    def post(self, request):
        seria = CommandeAjoutSerializer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            commande = Commande.objects.get(commande_id=request.query_params.get('commande_id'))
            commande.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        commande = Commande.objects.all()
        seria = GetCommandeSerializer(commande, many=True)
        return Response(status=200, data={'commande': seria.data})

class GetInstance(APIView):
    def get(self, request):
        try:
            commande = Commande.objects.get(commande_id=request.query_params.get('commande_id'))
            seria = GetCommandeSerializer(commande)
            return Response(status=status.HTTP_200_OK, data={'commande': seria.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
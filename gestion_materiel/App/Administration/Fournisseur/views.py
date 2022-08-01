from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from App.Administration.Fournisseur.serializers import AjoutSerializer, GetSerializer
from App.models import Fournisseur


class Crud(APIView):
    def post(self, request):
        seria = AjoutSerializer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            fournisseur_code = Fournisseur.objects.get(fournisseur_id=request.query_params.get('fournisseur_id'))
            fournisseur_code.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            fournisseur = Fournisseur.objects.get(pk=request.query_params.get('fournisseur_id'))
            seria = AjoutSerializer(data=request.data)
            if seria.is_valid():
                fournisseur.fournisseur_nom = seria.data['fournisseur_nom']
                fournisseur.fournisseur_prenom = seria.data['fournisseur_prenom']
                fournisseur.fournisseur_adresse = seria.data['fournisseur_adresse']
                fournisseur.fournisseur_telefone = seria.data['fournisseur_telefone']
                fournisseur.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        fournisseur = Fournisseur.objects.all()
        seria = GetSerializer(fournisseur, many=True)
        return Response(status=200, data={'fournisseur': seria.data})

class GetInstance(APIView):
    def get(self, request):
        try:
            fournisseur = Fournisseur.objects.get(fournisseur_id=request.query_params.get('fournisseur_id'))
            seria = GetSerializer(fournisseur)
            return Response(status=status.HTTP_200_OK, data={'fournisseur': seria.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
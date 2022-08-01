from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from App.models import Personel,Demande
from rest_framework import status

class AddSerializers(APIView):
    
    parser_classes = [MultiPartParser]

    def post(self,request):
        destinataire = Personel.objects.get(personnel_id = request.query_params.get('demande_personel_destinataire'))
        expediteur = Personel.objects.get(personel_id = request.query_params.get('demande_personel'))

        demande = Demande.objects.create(
            demande_personel = expediteur,
            demande_personel_destinataire = destinataire,
            demande_lien = request.data['demande_lien']
        )
        return Response(status=status.HTTP_201_CREATED)
        


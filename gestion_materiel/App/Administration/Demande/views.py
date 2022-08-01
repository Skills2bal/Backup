from rest_framework.parsers import MultiPartParser ,FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from App.models import Personel,Demande
from rest_framework import status
from .serializers import AddDemandeSerializer
from App.Administration.Personel.serializers import GetSerializerPersonnel

class Add(APIView):
    
    parser_classes = [MultiPartParser,FormParser,FileUploadParser]

    def post(self,request):
        print(request.data['demande_lien'])
        destinataire = Personel.objects.get(personel_id = request.query_params.get('demande_personel_destination'))
        expediteur = Personel.objects.get(personel_id = request.query_params.get('demande_personel'))

        demande = Demande.objects.create(
            demande_personel = expediteur,
            demande_personel_destination = destinataire,
            demande_lien = request.data['demande_lien']
        )

        data = {
            'demande' : AddDemandeSerializer(demande).data,
            'expediteur' : GetSerializerPersonnel(expediteur).data,
            'destinataire' : GetSerializerPersonnel(destinataire).data
        }
        return Response(status=status.HTTP_201_CREATED, data = data)


    def get(self,request):
        
        data = []
        demande = Demande.objects.all()
        for i in demande:
            expediteur = Personel.objects.get(personel_id = i.demande_personel.id)
            destinataire = Personel.objects.get(personel_id = i.demande_personel_destination.id)
            data.append(
                {
                'demande' : AddDemandeSerializer(i).data,
                'expediteur' : GetSerializerPersonnel(expediteur).data,
                'destinataire' : GetSerializerPersonnel(destinataire).data
                }
            )

        return Response(status=status.HTTP_200_OK, data = {'data' : data})
        

        


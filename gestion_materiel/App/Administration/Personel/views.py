from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




from .serializers import *

class Crud(APIView):
    def post(self,request):
        serial = AddSerializer(data = request.data)
        print(request.data)
        print(serial.is_valid())
        if serial.is_valid():
            personnel = Personel.objects.create_user(
                username = serial.data['personel_matricule'],
                password = serial.data['personel_nom'],
                personel_nom = serial.data['personel_nom'],
                personel_prenom = serial.data['personel_prenom'],
                personel_matricule =serial.data['personel_matricule'],
                personel_telefone = serial.data['personel_telefone'],
                personel_grade = serial.data['personel_grade'],
            )
            serial = GetSerializerPersonnel(personnel)
            return Response(status = status.HTTP_200_OK, data=serial.data)

        return Response(status = status.HTTP_400_BAD_REQUEST)


    def get(self,request):
        personnel = Personel.objects.all()
        serial = GetSerializerPersonnel(personnel,many=True)
        return Response(status = status.HTTP_200_OK, data=serial.data)
    
    


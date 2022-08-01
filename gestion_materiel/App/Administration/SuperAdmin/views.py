from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer
import requests
from django.contrib.auth import authenticate
from rest_framework import status
from gestion_materiel.settings import SERVER_ADRESS

class Login(APIView):
    
    def post(self,request):
        serial = LoginSerializer(data = request.data)
        if serial.is_valid():
            user = authenticate(username = serial.data['username'], password = serial.data['password'])
            if user:
                if user.is_superuser:
                    url = SERVER_ADRESS + 'administration/superadmin/obtaintoken/'
                    response = requests.post(url,json=serial.data)
                    if response.status_code == 200:
                        token = response.json()
                        return Response(status=status.HTTP_200_OK, data= token)
                    return Response(status=status.HTTP_400_BAD_REQUEST)

                return Response(status=status.HTTP_400_BAD_REQUEST)
    
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)
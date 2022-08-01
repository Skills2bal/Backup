from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

class Crud(APIView):

    def post(self,request):
        print(request.data)
        serial = CrudSerializer(data = request.data)
        if serial.is_valid():
            division = serial.save()
            serial = GetDivisionSerializer(division)
            return Response(status=status.HTTP_200_OK,data=serial.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        divisions = Division.objects.all()
        serial = GetDivisionSerializer(divisions,many=True)
        return Response(status=status.HTTP_200_OK, data= {'divisions': serial.data})


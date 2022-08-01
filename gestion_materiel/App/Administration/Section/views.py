#Importation
#from ast import Add
#from os import stat
#import re
from App.models import Division
from rest_framework.views import APIView
from rest_framework.response import Response
#from .serializer import *
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from App.Administration.Division import serializers
from App.Administration.Section.serializers import *
from App.models import Section


class Crud(APIView):
    def post(self, request):
        serial = AjoutSerializer(data = request.data)
        
        if serial.is_valid():
            
            section = serial.save()
            serial_s = GetSectionSerializer(section)
            serial_d = serializers.GetDivisionSerializer(section.division_division)
            datas = {'division' : serial_d.data,'section': serial_s.data}
            print(datas)
            return Response(status=status.HTTP_201_CREATED,data=datas)

        return Response(status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            section_code = Section.objects.get(section_id = request.query_params.get('section_id'))
            section_code.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            section = Section.objects.get(Section_id = request.query_params.get('section_id'))
            seria = AjoutSerializer(data = request.data)
            if seria.is_valid():
                section.section_code = seria.data['section_code']
                section.section_libelle = seria.data['section_libelle']
                section.division_division = seria.data['division_division']
                section.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        seria = Section.objects.all()
        seria = GetSectionSerializer(seria , many = True)
        return Response(status=status.HTTP_200_OK , data = {'sections' : seria.data})

class GetInstance(APIView):
    def get(self, request):
        try:
            section = Section.objects.get(section_id = request.query_params.get('section_id'))
            seria = GetSectionSerializer(section)
            return Response(status=status.HTTP_200_OK, data = {'section' : seria.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SectionDivision(APIView):
    
    def get(self,request):
        section = Section.objects.filter(division_division = request.query_params.get('division'))
        data = []
        for i in section:
            data.append(GetSectionSerializer(i).data)
        return Response(status = status.HTTP_200_OK, data = {'section': data})
 
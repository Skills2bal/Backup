
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from App.Administration.Section.serializers import GetSectionSerializer
from App.models import Section
from .serializers import *

class Crud(APIView):
    #fonction ajout
    def post(self, request):
        serial = BureauxSerializers(data = request.data)
        print(request.data)
        print(serial.is_valid())
        if serial.is_valid():
            section = Section.objects.get(section_id = serial.data['section_section'])
            bureau = Bureaux.objects.create(section_section = section,
                                            bureaux_code = serial.data['bureaux_code'],
                                            bureaux_libelle = serial.data['bureaux_libelle'])
            serial_bureau = GetBureauxSerializers(bureau)
            serial_section = GetSectionSerializer(bureau.section_section)
            datas = {'bureaux': serial_bureau.data, 'section': serial_section.data}
            print(datas)
            return Response(status=status.HTTP_201_CREATED, data = datas)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    #fonction Modifier
    def put(self, request):
        try:
            bureaux = Bureaux.objects.get(bureaux_id = request.query_params.get('bureaux_id'))
            serial = BureauxPutSerializers(data = request.data)
            if serial.is_valid():
                bureaux.bureaux_libelle = serial.data['bureaux_libelle']
                bureaux.save()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    
    #fonction Supprimer
    def delete(self, request):
        try:
            
            bureaux = Bureaux.objects.get(bureaux_id = request.qeury_params.get('bureaux_id'))
            bureaux.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #fonction Afficher tout
    def get(self, request):
        data = list()
        bureaux = Bureaux.objects.all()
        for i in bureaux:
            temp = {'bureaux' : GetBureauxSerializers(i).data , 'section' : GetSectionSerializer(i.section_section).data}
            data.append(temp)
        return Response(status=status.HTTP_200_OK, data = data)
    
class GetInstance(APIView):
    def get(self, request):
        try:
            bureaux = Bureaux.objects.get(bureaux_id = request.qeury_params.get('bureaux_id'))
            serial = GetBureauxSerializers(bureaux)
            return Response(status=status.HTTP_200_OK, data = {'bueaux': serial.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class GetBureauSection(APIView):

    def get(self,request):

        bureau = Bureaux.objects.filter(section_section = request.query_params.get('section'))
        data = []
        for i in bureau:
            data.append(
                    GetBureauxSerializers(i).data,
            )
        return Response(status=status.HTTP_200_OK, data = {'bureau': data})
from rest_framework.views import APIView
from App.models import *
from App.Administration.Fonction.serializers import *
from App.Administration.Personel.serializers import *
from App.Administration.Bureaux.serializers import *
from App.Administration.Section.serializers import *
from App.Administration.Division.serializers import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class AddSerializer(APIView):
    
    def post(self,request):
        
        serial = AddAffectationSerializer(data = request.data)
        if serial.is_valid():
            personnel = Personel.objects.get(personel_id = serial.data['personnel'])
            fonction = Fonction.objects.get(fonction_id = serial.data['fonction'])
            bureaux = Bureaux.objects.get(bureaux_id = serial.data['bureau'])
            affectation = Affecter.objects.create(
                personel_personel = personnel,
                fonction_fonction = fonction,
                bureaux_bureaux = bureaux,
            )

            section = Section.objects.get(section_id = bureaux.section_section.section_id)
            division = Division.objects.get(division_id = section.division_division.division_id)


            return Response(status = status.HTTP_201_CREATED, data= {
                'affectation' :GetAffectationSerializer(affectation).data,
                'fonction' : GetFonctionSerializers(fonction).data,
                'bureaux' : GetBureauxSerializers(bureaux).data,
                'division' : GetDivisionSerializer(division).data,
                'section': GetSectionSerializer(section).data
            })

        return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        personnel = Personel.objects.get(personel_id = request.query_params.get('personnel'))
        affectation  = Affecter.objects.filter(personel_personel = personnel)
        data = list()
        for i in affectation:
            bureaux = Bureaux.objects.get(bureaux_id = i.bureaux_bureaux.bureaux_id)
            fonction = Fonction.objects.get(fonction_id = i.fonction_fonction.fonction_id)
            section = Section.objects.get(section_id = bureaux.section_section.section_id)
            divison = Division.objects.get(division_id = section.division_division.division_id)

            data.append(
                {   
                    'affectation': GetAffectationSerializer(i).data,
                    'bureaux': GetBureauxSerializers(bureaux).data,
                    'section' : GetSectionSerializer(section).data,
                    'fonction' : GetFonctionSerializers(fonction).data,
                    'division' : GetDivisionSerializer(divison).data,
                }
            )

        return Response(status=status.HTTP_200_OK,data={'affectations': data})

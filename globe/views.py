from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import CountryListSerializer, CountrySerializer, ProvinceSerializer, ProvinceListSerializer, DistrictSerializer, SubDistrictSerializer, POISerializer
from .models import Country, Province, District, SubDistrict, POI

# Display all countries
class CountryListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountryListSerializer(countries, many=True)
        return Response(serializer.data)

# Display all provinces in a country
class ProvinceListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_province(self, adm0_pcode):
        try:
            return Province.objects.filter(adm0_pcode=adm0_pcode)
        except Province.DoesNotExist:
            raise NotFound(detail="Province not found", code=status.HTTP_404_NOT_FOUND)


    def get(self, _request, adm0_pcode):
        provinces = self.get_province(adm0_pcode=adm0_pcode)
        serializer = ProvinceListSerializer(provinces, many=True)
        return Response(serializer.data)
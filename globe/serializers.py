from rest_framework_gis import serializers
from .models import Country, Province, District, SubDistrict, POI

class CountrySerializer(serializers.GeoModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountryListSerializer(serializers.GeoModelSerializer):
    class Meta:
        model = Country
        fields = ('adm0_pcode', 'adm0_en', 'adm0_th', 'pk')

class ProvinceSerializer(serializers.GeoModelSerializer):
    class Meta:
        model = Province
        # geo_field = 'geom'
        fields = '__all__'

class ProvinceListSerializer(serializers.GeoModelSerializer):
    class Meta:
        model = Province
        geo_field = 'geom'
        fields = ('adm1_pcode', 'adm1_en', 'adm1_th', 'adm0_en', geo_field)

class DistrictSerializer(serializers.GeoModelSerializer):
    class Meta:
        model = District
        geo_field = 'geom'
        fields = '__all__'

class SubDistrictSerializer(serializers.GeoModelSerializer):
    class Meta:
        model = SubDistrict
        geo_field = 'geom'
        fields = '__all__'

class POISerializer(serializers.GeoModelSerializer):
    class Meta:
        model = POI
        fields = '__all__'

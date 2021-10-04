from django.contrib.gis import admin
from .models import Country, Province, District, SubDistrict, POI
# Register your models here.

admin.site.register(Country, admin.OSMGeoAdmin)
admin.site.register(Province, admin.OSMGeoAdmin)
admin.site.register(District, admin.OSMGeoAdmin)
admin.site.register(SubDistrict, admin.OSMGeoAdmin)
admin.site.register(POI, admin.OSMGeoAdmin)

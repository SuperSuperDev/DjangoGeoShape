from django.contrib import admin
from .models import thailandPlaces, thailandShapes, Country, Province, District, SubDistrict

# Register your models here.

admin.site.register(thailandPlaces)
admin.site.register(thailandShapes)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(SubDistrict)

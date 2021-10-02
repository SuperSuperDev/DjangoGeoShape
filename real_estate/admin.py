from django.contrib import admin
from .models import Address, thailandPlaces, Image, Property_Listing

# Register your models here.
admin.site.register(Property_Listing)
admin.site.register(Image)
admin.site.register(Address)
#admin.site.register(thailandPlaces)
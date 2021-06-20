from rest_framework import serializers
from .models import Property_Listing, Image, Country

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = '__all__'
class PropertyListingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Property_Listing
        fields = '__all__'

class PopulatedPropertyListingSerializer(PropertyListingSerializer):
    images = ImageSerializer(many=True)
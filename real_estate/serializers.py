from rest_framework import serializers
from .models import Property_Listing, Image, Address

class AddressSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(many=False)
    region = serializers.StringRelatedField(many=False)
    subregion = serializers.StringRelatedField(many=False)
    city = serializers.StringRelatedField(many=False)
    class Meta:
            model = Address
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
    address = AddressSerializer(many=False)
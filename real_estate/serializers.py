from rest_framework import serializers
from .models import Property_Listing

class PropertyListingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Property_Listing
        fields = '__all__'


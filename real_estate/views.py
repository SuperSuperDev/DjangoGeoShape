# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
# from django.views import View

# Create your views here.

from .models import Property_Listing
from .serializers import PropertyListingSerializer 
class PropertyListingListView(APIView):

    def get(self, _request):
        property_listings = Property_Listing.objects.all()
        serialized_property_listings = PropertyListingSerializer(property_listings, many=True)
        return Response(serialized_property_listings.data, status=status.HTTP_200_OK)

class PropertyListingDetailView(APIView):
    
    def get(self, _request, pk):
        try:
            property_listing = Property_Listing.objects.get(pk=pk)
            serialized_property_listing = PropertyListingSerializer(property_listing)
            return Response(serialized_property_listing.data, status=status.HTTP_200_OK)
        except Property_Listing.DoesNotExist:
            raise NotFound()


# class PropertyListingListView(View):

#     def get(self, request):
#         property_listings = Property_Listing.objects.all()
#         return render(request, 'index.html', {'property_listings' : property_listings})

# class PropertyListingDetailView(View):

#     def get(self, request, pk):
#         property_listing = Property_Listing.objects.get(pk=pk)

#         return render(request, 'show.html', {'property_listing' : property_listing})

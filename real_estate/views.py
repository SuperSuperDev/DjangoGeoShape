# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
# from django.views import View

# Create your views here.

from .models import Country, Property_Listing, Image
from .serializers import CountrySerializer, PropertyListingSerializer, PopulatedPropertyListingSerializer, ImageSerializer 

class CountryListView(APIView):

    def get(self, _request):
        countries = Country.objects.all()
        serialized_countries = CountrySerializer(countries, many=True)
        return Response(serialized_countries.data, status=status.HTTP_200_OK)
        
class PropertyListingListView(APIView):

    def get(self, _request):
        property_listings = Property_Listing.objects.all()
        serialized_property_listings = PopulatedPropertyListingSerializer(property_listings, many=True)
        return Response(serialized_property_listings.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        new_property_listing = PropertyListingSerializer(data=request.data)
        if new_property_listing.is_valid():
            new_property_listing.save()
            return Response(new_property_listing.data, status=status.HTTP_201_CREATED)
        return Response(new_property_listing.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class PropertyListingDetailView(APIView):

    def get_Property_Listing(self, pk):
        try:
            return Property_Listing.objects.get(pk=pk)
        except Property_Listing.DoesNotExist:
            raise NotFound()
    
    def get(self, _request, pk):
        property_listing = self.get_Property_Listing(pk=pk)
        serialized_property_listing = PopulatedPropertyListingSerializer(property_listing)
        return Response(serialized_property_listing.data, status=status.HTTP_200_OK)
        

    def delete(self, _request, pk):
        property_listing_to_delete = self.get_Property_Listing(pk=pk)
        property_listing_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        property_listing_to_update = self.get_Property_Listing(pk=pk)
        updated_property_listing = PropertyListingSerializer(property_listing_to_update, data=request.data)
        if updated_property_listing.is_valid():
            updated_property_listing.save()
            return Response(updated_property_listing.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_property_listing.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ImageListView(APIView):

    def post(self, request, plist_pk):
        request.data['property_listing'] = plist_pk
        serialized_image = ImageSerializer(data=request.data)
        if serialized_image.is_valid():
            serialized_image.save()
            return Response(serialized_image.data, status=status.HTTP_201_CREATED)
        return Response(serialized_image.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ImageDetailView(APIView):

    def delete(self, _request, _plist_pk, image_pk):
        try:
            image_to_delete = Image.objects.get(pk=image_pk)
            image_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Image.DoesNotExist:
            raise NotFound()

# class PropertyListingListView(View):

#     def get(self, request):
#         property_listings = Property_Listing.objects.all()
#         return render(request, 'index.html', {'property_listings' : property_listings})

# class PropertyListingDetailView(View):

#     def get(self, request, pk):
#         property_listing = Property_Listing.objects.get(pk=pk)

#         return render(request, 'show.html', {'property_listing' : property_listing})

from django.shortcuts import render
from django.views import View
# Create your views here.

from .models import Property_Listing

class PropertyListingListView(View):

    def get(self, request):
        property_listings = Property_Listing.objects.all()
        return render(request, 'index.html', {'property_listings' : property_listings})

class PropertyListingDetailView(View):

    def get(self, request, pk):
        property_listing = Property_Listing.objects.get(pk=pk)

        return render(request, 'show.html', {'property_listing' : property_listing})

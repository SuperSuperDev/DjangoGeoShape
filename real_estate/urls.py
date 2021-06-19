from django.urls import path
from .views import PropertyListingDetailView, PropertyListingListView

urlpatterns = [
    path('', PropertyListingListView.as_view()),
    path('<int:pk>/', PropertyListingDetailView.as_view())
]
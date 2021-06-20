from django.urls import path
from .views import ImageDetailView, ImageListView, PropertyListingListView, PropertyListingDetailView

urlpatterns = [
    path('', PropertyListingListView.as_view()),
    path('<int:pk>/', PropertyListingDetailView.as_view()),
    path('<int:plist_pk>/images/', ImageListView.as_view()),
    path('<int:_plist_pk>/images/<int:image_pk>/', ImageDetailView.as_view()),
]
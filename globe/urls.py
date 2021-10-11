from django.urls import path
from .views import CountryListView, ProvinceListView


urlpatterns = [
    path('', CountryListView.as_view(), ),
    path('<adm0_pcode>/', ProvinceListView.as_view(), ),
]

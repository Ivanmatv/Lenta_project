from rest_framework import viewsets, status
from rest_framework.response import Response
from categories.models import Sales
from categories.models import Shops, Categories, Sales, Forecast
from  .serializers import ShopsSerializer, CategoriesSerializer, ForecastSerializer, SalesSerializer


class ShopsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =Categories.objects.all()
    serializer_class = CategoriesSerializer


class SalesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
  

class ForecastViewSet(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get', 'post']
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

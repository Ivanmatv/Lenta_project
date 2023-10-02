from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .models import Forecast, Sales, Shops
from .serializers import (
    ForecastSerializer,
    SalesSerializer,
    ShopSerializer
)


class SaleViewSet(viewsets.ModelViewSet):
    """Представления для покупок."""
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filter_backends = (DjangoFilterBackend, )


class ShopViewSet(viewsets.ModelViewSet):
    """Представления для магазинов."""
    queryset = Shops.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (DjangoFilterBackend, )


class ForecastViewSet(viewsets.ModelViewSet):
    """Представления для прогнозов."""
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

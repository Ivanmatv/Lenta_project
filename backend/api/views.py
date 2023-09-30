from rest_framework import viewsets
from .models import Category, Sales, Shop, Forecast
from .serializers import(
    CategorySerializer,
    ForecastSerializer,
    SalesSerializer,
    ShopSerializer
)


class SalesViewSet(viewsets.ModelViewSet):
    """Представления для покупок."""
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class ShopViewSet(viewsets.ModelViewSet):
    """Представления для магазинов."""
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ForecastViewSet(viewsets.ModelViewSet):
    """Представления для прогнозов."""
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

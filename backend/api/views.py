from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Categories, Forecast, Sales, Shops
from .serializers import (
    CategoriesSerializer,
    ForecastSerializer,
    SalesSerializer,
    ShopSerializer
)


class ShopViewSet(viewsets.ModelViewSet):
    """Представления для магазинов."""
    queryset = Shops.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (DjangoFilterBackend, )


class ForecastViewSet(viewsets.ModelViewSet):
    """Представления для прогнозов."""
    http_method_names = ['get', 'post']
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SalesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    def list(self, request, *args, **kwargs):
        date = request.query_params.get('date', None)
        context = {'date': date}
        serializer = self.get_serializer(
            self.queryset,
            many=True,
            context=context
        )
        return Response(serializer.data)

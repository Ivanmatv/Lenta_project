from rest_framework import serializers, viewsets, routers
from .models import Category, Sales, Shop, Forecast


class ShopSerializer(serializers.ModelSerializer):
    """Сериализатор для магазинов."""
    class Meta:
        model = Shop
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):
    """Сериализатор для покупок."""
    class Meta:
        model = Sales
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор для прогнозов."""
    class Meta:
        model = Forecast
        fields = '__all__'

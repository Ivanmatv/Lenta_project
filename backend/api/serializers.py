from rest_framework import serializers

from .models import Forecast, Shops


class ShopSerializer(serializers.ModelSerializer):
    """Сериализатор для магазинов."""
    class Meta:
        model = Shops
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор для прогнозов."""
    forecast = serializers.JSONField()

    class Meta:
        model = Forecast
        fields = '__all__'

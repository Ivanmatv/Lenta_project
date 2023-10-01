from rest_framework import serializers
from .models import Category, Sales, SalesFact, Shop, Forecast


class ShopSerializer(serializers.ModelSerializer):
    """Сериализатор для магазинов."""
    class Meta:
        model = Shop
        fields = '__all__'


class SalesFactSerializer(serializers.Serializer):
    """Сериализатор для информаии о товаре."""
    date = serializers.DateField()
    sales_type = serializers.IntegerField()
    sales_units = serializers.IntegerField()
    sales_units_promo = serializers.IntegerField()
    sales_rub = serializers.DecimalField(max_digits=10, decimal_places=2)
    sales_run_promo = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = SalesFact
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):
    """Сериализатор для покупок."""
    store = serializers.StringRelatedField(read_only=True)
    sku = serializers.StringRelatedField(read_only=True)
    fact = SalesFactSerializer(many=True)

    class Meta:
        model = Sales
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор для прогнозов."""
    forecast = serializers.DictField()

    class Meta:
        model = Forecast
        fields = '__all__'

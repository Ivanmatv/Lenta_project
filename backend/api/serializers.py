from rest_framework import serializers
from django.db import models

from categories.models import Categories, Shops, Sales, Forecast

class CategoriesSerializer(serializers.ModelSerializer):
    sku = serializers.CharField()
    group = serializers.CharField()
    category = serializers.CharField()
    subcategory = serializers.CharField()
    uom = serializers.IntegerField()
#    date = models.DateField()
    class Meta:
        model = Categories
        fields = '__all__'
        read_only_fields = '__all__',


class SalesFactSerializer(serializers.Serializer):
#    date = serializers.DateField()
    sales_type = serializers.IntegerField()
    sales_units = serializers.IntegerField()
    sales_units_promo = serializers.IntegerField()
    sales_rub = serializers.DecimalField(max_digits=10, decimal_places=2)
    sales_run_promo = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Sales
        fields = '__all__'

class SalesSerializer(serializers.Serializer):
#    fact = SalesFactSerializer(many=True)
    class Meta:
        model = Sales
#        fields = ['store', 'sku', 'fact']
        fields = '__all__'

class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = '__all__'

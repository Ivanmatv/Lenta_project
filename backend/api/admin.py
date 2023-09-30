from django.contrib import admin
from .models import Category, Forecast, Sales, Shop


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('store', 'sku')
    search_fields = ('store',)
    list_filter = ('store', 'sku')
    empty_value_display = '-пусто-'


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'store', 'city', 'division',
        'type_format', 'loc', 'size', 'is_active'
    )
    search_fields = ('store', 'city', 'division',)
    list_filter = (
        'store', 'city', 'division',
        'type_format', 'loc', 'size', 'is_active'
    )
    empty_value_display = '-пусто-'


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('store', 'forecast_date')
    search_fields = ('store', 'forecast_date')
    list_filter = ('store', 'forecast_date')
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'sku', 'group', 'category',
        'subcategory', 'uom'
    )
    search_fields = ('group', 'category', 'subcategory')
    empty_value_display = '-пусто-'

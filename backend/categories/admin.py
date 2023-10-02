from django.contrib import admin
from .models import Categories, Sales, Shops, Forecast


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'category', 'subcategory', 'sku', 'uom')
    list_filter = ('group', 'category', 'subcategory', 'sku',)


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'store', 'sku', 'sales_type','sales_units','sales_units_promo','sales_rub','sales_run_promo')
    list_filter = ('store', 'sku',)


@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ('store', 'city', 'division', 'type_format', 'loc', 'size', 'is_active')
    list_filter = ('store','city', 'division',) 


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('id', 'forecast_date', 'store', 'forecast')
#   ordering = ('category','uom',)

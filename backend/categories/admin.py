from django.contrib import admin
from .models import Categories, Sales, Shops, Forecast


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id','sku', 'store', 'sales_type','sales_units','sales_units_promo','sales_rub','sales_run_promo')
    list_filter = ('store','sku',) #'date',)
#    ordering = ('date',)



@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ('id','store', 'city', 'division', 'type_format', 'loc')
    list_filter = ('store','city', 'division',) 


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'category','sku', 'uom')
    list_filter = ('group', 'category', 'subcategory', 'sku',)
    search_fields = ('sku', )



@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('id', 'forecast_date', 'store', 'forecast')
#   ordering = ('category','uom',)


from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet,
                    ForecastViewSet,
                    SaleViewSet,
                    ShopViewSet,
                    )

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'shops', ShopsViewSet, basename='shops')
router_v1.register(r'categories', CategoriesViewSet, basename='categories')
router_v1.register(r'sales', SalesViewSet, basename='sales')
router_v1.register(r'forecast', ForecastViewSet, basename='forecast')

urlpatterns = [
    path('', include(router_v1.urls)),
]

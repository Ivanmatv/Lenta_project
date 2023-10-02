from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (ForecastViewSet,
                    SaleViewSet,
                    ShopViewSet,
                    )

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'shops', ShopViewSet, basename='shops')
# router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(r'sales', SaleViewSet, basename='sales')
router_v1.register(r'forecast', ForecastViewSet, basename='forecast')

urlpatterns = [
    path('', include(router_v1.urls)),
]

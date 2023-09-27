from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet, UserViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'shops', IngredientViewSet, basename='shops')
router_v1.register(r'categories', TagViewSet, basename='categories')
router_v1.register(r'forecast', RecipeViewSet, basename='forecast')
router_v1.register(r'sales', UserViewSet, basename='sales')
router_v1.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

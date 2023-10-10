from django.urls import include, path

from rest_framework import routers

from .views import CustomUserViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.url')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

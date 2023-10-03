from django.urls import include, path
from rest_framework import routers
from django.contrib.auth import views as auth_views

from .views import CustomUserViewSet

v1_router = routers.DefaultRouter()
v1_router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
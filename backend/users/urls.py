from django.urls import include, path
from rest_framework import routers
from django.contrib.auth import views as auth_views

from .views import CustomUserViewSet

v1_router = routers.DefaultRouter()
v1_router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.authtoken')),
    path('v1/auth/', include('djoser.urls.jwt')),
]

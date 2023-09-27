from django.urls import include, path
from rest_framework import routers

from .views import CustomUserViewSet

v1_router = routers.DefaultRouter()
v1_router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
]

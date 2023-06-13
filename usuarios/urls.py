from django.contrib import admin
from django.urls import path, include
from .views import CustomUserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', CustomUserViewSet, basename='Usuarios')
router.register(r'token', CustomTokenObtainPairView, basename='Access Token')
router.register(r'refrescar', CustomTokenRefreshView, basename='Refresh Token')

urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib import admin
from django.urls import path, include
from .views import CustomUserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', CustomUserViewSet, basename='Usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='Access Token'),
    path('refrescar/', CustomTokenRefreshView.as_view(), name='Refresh Token'),
]

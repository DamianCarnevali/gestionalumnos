from django.contrib import admin
from django.urls import path, include
from .views import CustomUserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', CustomUserViewSet)
router.register(r'token', CustomTokenObtainPairView)
router.register(r'refrescar', CustomTokenRefreshView)

urlpatterns = [
    path('', include(router.urls)),
]

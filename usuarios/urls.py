from django.urls import path, include
from rest_framework import routers
from .views import UsuariosViewSet

routers = routers.DefaultRouter()
routers.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
from django.urls import path, include
from rest_framework import routers
from .views import MateriasViewSet, CarrerasViewSet

routers = routers.DefaultRouter()
routers.register(r'', MateriasViewSet)
routers.register(r'', CarrerasViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
from django.urls import path, include
from rest_framework import routers
from .views import ProfesoresViewSet, DetallesProfesoresViewSet, ProfesoresCompletosViewSet, ProfesoresMateriasViewSet

routers = routers.DefaultRouter()
routers.register(r'', ProfesoresViewSet)
routers.register(r'', DetallesProfesoresViewSet)
routers.register(r'', ProfesoresCompletosViewSet)
routers.register(r'', ProfesoresMateriasViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
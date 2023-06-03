from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Gestión de Alumnos API",
        default_version='v1',
        description="Sistema de Gestión de Alumnos para el Instituto Superior de Formación Docente y Técnica N° 239",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/', include('estudiantes.urls')),
    path('documentacion/', schema_view.with_ui('swagger')),
    path('usuarios/', include('usuarios.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refrescar/', TokenRefreshView.as_view()),
]

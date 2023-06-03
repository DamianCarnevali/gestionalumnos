from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views_token import TokenView
from rest_framework_simplejwt.views import TokenRefreshView
...

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
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenView.as_view()),
    path('refrescartoken/', TokenRefreshView.as_view()),
    path('estudiantes/', include('estudiantes.urls')),
    path('documentacion/', schema_view.with_ui('swagger')),
    path('usuarios/', include('usuarios.urls')),
]

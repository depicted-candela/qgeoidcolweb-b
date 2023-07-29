from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("subir_archivos", views.subir_archivos, name="subir_archivos"),
    path("recibir", views.RecibirDatosReactViewSet.as_view(), name="recibir_datos"),
    # path("api/recibir_datos_react", views.RecibirDatosReact.as_view(), name="recibir_datos_react"),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("entrar", views.entrar, name="entrar"),
    path("registro", views.registro, name="registro"),
    path("salir", views.salir, name="salir"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
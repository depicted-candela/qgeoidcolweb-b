from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("subir_archivos", views.subir_archivos, name="subir_archivos"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("entrar", views.entrar, name="entrar"),
    path("registro", views.registro, name="registro"),
    path("salir", views.salir, name="salir"),
]
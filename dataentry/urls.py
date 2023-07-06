from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("subir_archivos", views.subir_archivos, name="subir_archivos"),
    path("entrar", views.entrar, name="entrar"),
    path("registro", views.registro, name="registro"),
    path("salir", views.salir, name="salir"),
]
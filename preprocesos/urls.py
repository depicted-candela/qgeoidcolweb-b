from django.urls import path

from . import views

urlpatterns = [
    path("prjs_terrestres", views.prjs_terrestres, name="prjs_terrestres"),
    path("mostrar_prjs_terr", views.mostrar_prjs_terr, name="mostrar_prjs_terr"),
]
from django.urls import path

from . import views

urlpatterns = [
    path("prjs_terrestres", views.prjs_terr, name="prjs_terrestres"),
    path("csrf_token", views.get_csrf_token, name="csrf_token"),
    path("mostrar_prjs_terr", views.mostrar_prjs_terr, name="mostrar_prjs_terr"),
    path("api/rcbr_args_prjs_trr", views.rcbr_args_prjs_trr, name="recibir_args_prjs_terr"),
]
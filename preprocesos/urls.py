from django.urls import path

from . import views


urlpatterns = [
    path("mostrar_prjs_terr/", views.mostrar_prjs_terr, name="mostrar_prjs_terr"),
    path("prjs_terrestres", views.prjs_terr, name="prjs_terrestres"),
    path("csrf_token", views.CsrfTokenView.as_view(), name="csrf_token"),
    path("recibir_preprocesar_api", views.RecibirInfoPreprocess.as_view(), name="recibir_preprocesar_api"),
    path("recibir_preprocesar", views.recibir_info_preprocess, name="recibir_preprocesar"),
]
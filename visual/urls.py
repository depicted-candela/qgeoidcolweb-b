from django.urls import path

from . import views


urlpatterns = [
    path('enviar_proyectos_visuales', views.getProjectNames.as_view(), name="enviar_proyectos_visuales"),
]
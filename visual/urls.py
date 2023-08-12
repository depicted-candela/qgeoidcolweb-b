from django.urls import path

from . import views


urlpatterns = [
    path('enviar_proyectos_visuales', views.getProjectNames.as_view(), name="enviar_proyectos_visuales"),
    path('enviar_puntos_visuales', views.getDataProjects.as_view(), name="enviar_puntos_visuales"),
]
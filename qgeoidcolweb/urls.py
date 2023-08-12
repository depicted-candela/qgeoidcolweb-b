from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("visual/", include("visual.urls")),
    path("preprocesos/", include("preprocesos.urls")),
    path("", include("dataentry.urls"))
]

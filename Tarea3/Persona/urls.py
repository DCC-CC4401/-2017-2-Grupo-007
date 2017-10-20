from django.conf.urls import url
from Persona.views import home

urlpatterns = (
    url(r'^$', home, name="home"),
)
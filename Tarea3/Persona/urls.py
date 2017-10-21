from django.conf.urls import url
from Persona.views import home
from Persona.views import signup
urlpatterns = (
    url(r'^$', home, name="home"),
    url(r'^/signup/$', signup, name="signup"),
)
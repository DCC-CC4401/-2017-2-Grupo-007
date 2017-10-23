from django.conf.urls import url
from Persona.views import home
from Persona.views import signup, mylogout


urlpatterns = (
    url(r'^$', home, name="home"),
    url(r'^signup/$', signup, name="signup"),
    url(r'^logout/$', mylogout, name="logout")
)
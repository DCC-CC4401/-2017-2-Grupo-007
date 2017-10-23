from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.enadopcion, name='enadopcion'),
    url(r'^(?P<animal_id>[0-9]+)/$', views.ficha, name='ficha'),
]
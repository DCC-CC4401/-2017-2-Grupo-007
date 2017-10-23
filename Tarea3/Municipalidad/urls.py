from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.muni, name='muni'),
    url(r'^tablas/$', views.tablas, name='tablas'),
    url(r'^ultimasdenuncias/$', views.ultimasdenuncias, name='ultimasdenuncias'),
    url(r'^(?P<denuncia_id>[0-9]+)/$', views.detalles, name='detalles'),
    url(r'^gestion/(?P<denuncia_id>[0-9]+)/$', views.gestion, name='gestion')
]
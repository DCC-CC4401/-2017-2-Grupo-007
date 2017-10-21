from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.muni, name='muni'),
    url(r'^tablas/$', views.tablas, name='tablas'),
    url(r'^ultimasdenuncias/$', views.ultimasdenuncias, name='ultimasdenuncias')
]
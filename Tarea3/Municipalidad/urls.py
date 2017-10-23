from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.muni, name='muni'),
    url(r'^tablas/$', views.tablas, name='tablas'),
    url(r'^ultimasdenuncias/$', views.ultimasdenuncias, name='ultimasdenuncias'),
    url(r'^(?P<denuncia_id>[0-9]+)/$', views.detalles, name='detalles'),
<<<<<<< HEAD
    url(r'^chartsPageMuni/$', views.chartsPageMuni, name='chartsPageMuni')

=======
    url(r'^gestion/(?P<denuncia_id>[0-9]+)/$', views.gestion, name='gestion')
>>>>>>> c67920e38b6634382886ebe087c67d8c2c45df0d
]
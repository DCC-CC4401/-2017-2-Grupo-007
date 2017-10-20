from django.conf.urls import url
from Denuncia.views import denunciar

urlpatterns = (
    url(r'^$', denunciar, name="denunciar"),
)
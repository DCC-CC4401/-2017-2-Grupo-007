from django.conf.urls import url
from ONG.views import onghome

urlpatterns = (
    url(r'^$', onghome, name="onghome"),
)
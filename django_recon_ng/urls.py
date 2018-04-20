from django.conf.urls import url

from .views	 import recon_graph

urlpatterns = [
	url(r'^graph', recon_graph),
]
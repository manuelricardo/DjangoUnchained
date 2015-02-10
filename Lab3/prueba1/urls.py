from django.conf.urls import patterns, url
from prueba1 import views

urlpatterns = patterns('',
	url(r'^$', views.index , name='index'),
	#url(r'^mensaje2/$', views.mensaje2, name='mensaje2'),
)
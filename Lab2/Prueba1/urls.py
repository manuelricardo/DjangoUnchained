from django.conf.urls import patterns, url
from Prueba1 import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^otra/$', views.otra, name='otra'),
)

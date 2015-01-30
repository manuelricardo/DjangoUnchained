from django.conf.urls import patterns, include, url
from django.contrib import admin
from Prueba1 import views

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	url(r'^prueba/', include('Prueba1.urls')),
	url(r'^otra/', views.otra, name='otra'),
)
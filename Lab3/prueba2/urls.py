from django.conf.urls import patterns, include, url
from prueba2 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lab3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', views.index, name='index'),

)

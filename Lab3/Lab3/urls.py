from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lab3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('prueba1.urls')),
    url(r'^prueba2/', include('prueba2.urls'))

)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'^uploads/(?P<path>.*)',
		'serve',
		{
			'document_root': settings.MEDIA_ROOT
		}),
	)
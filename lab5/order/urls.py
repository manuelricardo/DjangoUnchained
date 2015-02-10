from django.conf.urls import patterns, include, url
from order import views

urlpatterns = patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^detail/(?P<order_id>\d+)/$',views.order, name='order'),
	url(r'^customer/(?P<customer_id>\d+)/$',views.customer, name='customer'),
	url(r'^product/(?P<product_id>\d+)/$',views.product, name='product'),
)
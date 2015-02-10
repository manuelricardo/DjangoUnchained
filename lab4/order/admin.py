from django.contrib import admin
	
# Register your models here.
from order.models import Customer, Product, Stock, Order

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Order)
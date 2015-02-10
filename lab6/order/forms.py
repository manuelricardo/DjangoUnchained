#-*- encoding:utf-8 -*-
from django	import forms
from order.models import Customer, Order, Product, Stock

class CustomerForm(forms.ModelForm):
	customer_name = forms.CharField(max_length=128, help_text='Nombre del Cliente: ')
	customer_address = forms.CharField(max_length=64, help_text='Dirección del Cliente: ')
	customer_phone = forms.CharField(max_length=24, help_text='Teléfono del Cliente: ')

	class Meta:
		model = Customer
		fields = ('customer_name', 'customer_address', 'customer_phone',)
		excludes = ('date_created_customer', 'date_updated_customer',)

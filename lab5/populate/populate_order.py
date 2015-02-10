import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import lab4

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab4.settings')

# Importando modelos de la aplicación Order

from order.models import Customer, Product, Stock, Order

# Preparando Script para trabajar con un entorno de configuración Django

import django
django.setup()

#Función para crear los datos en la base de datos

def populate():
	customer_one = add_customer(
		customer_name='Ana María Avila',
		customer_address= 'Cr 20 No. 14 23',
		customer_phone= '3044664435')

	product_one = add_product(
		product_name= 'Tablet Galaxy 3',
		product_price=300000,
		product_type='Tablet',
		product_description='Tablet de 8 pulgadas Android')

	stock_one = add_stock(
		stock_product_id=product_one,
		stock_quantity=7)

	order_one = add_order(
		order_customer_id=customer_one,
		order_product_id=product_one,
		order_amount=4)

	for product in Product.objects.all():
		for stock in Stock.objects.filter(stock_product_id=product):
			print("El producto {0} tiene un stock de {1} unidades".format(str(product),str(stock.stock_quantity)))

	for customer in Customer.objects.all():
		for order in Order.objects.filter(order_customer_id=customer):
			print("El cliente {0} tiene una orden con #{1}".format(str(customer),str(order.id)))

def add_product(**kwargs):
	product = Product.objects.get_or_create(
		product_name=kwargs['product_name'],
		product_price=kwargs['product_price'],
		product_type=kwargs['product_type'],
		product_description=kwargs['product_description'])[0]
	return product

def add_customer(**kwargs):
	customer = Customer.objects.get_or_create(
		customer_name=kwargs['customer_name'],
		customer_address=kwargs['customer_address'],
		customer_phone=kwargs['customer_phone'])[0]

	return customer

def add_stock(**kwargs):
	stock = Stock.objects.get_or_create(
		stock_product_id=kwargs['stock_product_id'],
		stock_quantity=kwargs['stock_quantity'])[0]
	return stock

def add_order(**kwargs):
	order = Order.objects.get_or_create(
		order_customer_id=kwargs['order_customer_id'],
		order_product_id=kwargs['order_product_id'],
		order_amount=kwargs['order_amount'])[0]
	return order

if __name__ == '__main__':
	print('Creando info en la Base de Datos')
	populate()
from order.models import Customer, Product, Stock, Order
from autofixture import generators, register, AutoFixture

import random

types = ('Hardware', 'Software', 'Test Software', 'Test Hardware', 'Apps', 'Big Data')
products = ('Casio 33W', 'Lumia 34', 'Cable USB', 'Quanta 4G', 'Magic Mouse', 'Moto G', 'Moto X',)

""" Clase para crear información para el modelo Customer """

class CustomerFixture(AutoFixture):
	field_values = {
		'customer_name': generators.FirstNameGenerator(), 
		'customer_address': generators.SmallIntegerGenerator(min_value=1240, max_value=9999),
		'customer_phone': generators.IntegerGenerator(min_value=124000, max_value=9999999)
	}

""" Clase para crear información para el modelo Product """

class ProductFixture(AutoFixture):
	field_values = {
		'product_name': random.choice(products), 
		'customer_price': generators.PositiveIntegerGenerator(),
		'customer_type': random.choice(types),
		'product_description': generators.LoremGenerator()
	}

""" Clase para crear información para el modelo Stock """

class StockFixture(AutoFixture):
	field_values = {
		'stock_quantity': generators.SmallIntegerGenerator(min_value=1240, max_value=9999), 
	}

""" Asociando modelo a clase para generar informaćión """
register(Customer, CustomerFixture)
register(Product, ProductFixture)
register(Stock, StockFixture)
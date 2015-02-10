from django.db import models

# Create your models here.
class Customer(models.Model):
	customer_name = models.CharField(max_length=128,
		blank=True, null=True,
		verbose_name='Nombre',
		help_text='Ingrese el Nombre Completo.')

	customer_address = models.CharField(max_length=64,
		blank=True, null=True,
		verbose_name='Dirección',
		help_text='Ingrese la dirección del Cliente.')		
		
	customer_phone = models.CharField(max_length=24,
		blank=True, null=True,
		verbose_name='Teléfono',
		help_text='Ingrese el teléfono del Cliente.')	

	def __str__(self):
		return self.customer_name

class Product(models.Model):
	product_name = models.CharField(max_length=128,
		blank=True, null=True,
		verbose_name='Nombre',
		help_text='Ingrese el Nombre del Producto.')

	product_price = models.DecimalField(max_digits=64,
		decimal_places=2,
		verbose_name= 'Precio',
		help_text='Precio del Producto')

	product_type = models.CharField(max_length=128,
		blank=True, null=True,
		verbose_name='Tipo de Producto',
		help_text='Ingrese el tipo de producto al que pertenece')

	product_description = models.TextField(max_length=400,
		verbose_name='Descripción de producto',
		help_text='Ingrese la Descripción del Producto')

	def __str__(self):
		return self.product_name

class Stock(models.Model):
	stock_product_id = models.ForeignKey('Product')
	stock_quantity = models.IntegerField(max_length=24,
		verbose_name='Cantidad del producto',
		help_text='Ingrese la cantidad disponible del producto')
	

class Order(models.Model):
	order_customer_id = models.ForeignKey('Customer')
	order_product_id = models.ForeignKey('Product')
	order_amount = models.IntegerField(max_length=10,
		verbose_name='Cantidad de productos',
		help_text='Ingrese la cantidad de productos en la orden')
	order_date = models.DateField(auto_now=True)
	
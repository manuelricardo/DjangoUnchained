# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('customer_name', models.CharField(help_text='Ingrese el Nombre Completo.', null=True, blank=True, verbose_name='Nombre', max_length=128)),
                ('customer_address', models.CharField(help_text='Ingrese la dirección del Cliente.', null=True, blank=True, verbose_name='Dirección', max_length=64)),
                ('customer_phone', models.CharField(help_text='Ingrese el teléfono del Cliente.', null=True, blank=True, verbose_name='Teléfono', max_length=24)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('order_amount', models.IntegerField(help_text='Ingrese la cantidad de productos en la orden', verbose_name='Cantidad de productos', max_length=10)),
                ('order_date', models.DateField(auto_now=True)),
                ('order_customer_id', models.ForeignKey(to='order.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('product_name', models.CharField(help_text='Ingrese el Nombre del Producto.', null=True, blank=True, verbose_name='Nombre', max_length=128)),
                ('product_price', models.DecimalField(help_text='Precio del Producto', max_digits=64, decimal_places=2, verbose_name='Precio')),
                ('product_type', models.CharField(help_text='Ingrese el tipo de producto al que pertenece', null=True, blank=True, verbose_name='Tipo de Producto', max_length=128)),
                ('product_description', models.TextField(help_text='Ingrese la Descripción del Producto', verbose_name='Descripción de producto', max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('stock_quantity', models.IntegerField(help_text='Ingrese la cantidad disponible del producto', verbose_name='Cantidad del producto', max_length=24)),
                ('stock_product_id', models.ForeignKey(to='order.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='order_product_id',
            field=models.ForeignKey(to='order.Product'),
            preserve_default=True,
        ),
    ]

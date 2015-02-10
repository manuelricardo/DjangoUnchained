# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150209_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created_order',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 20, 55, 55, 628344, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date_updated_order',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 20, 56, 0, 285274, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date_created_product',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 20, 56, 5, 772704, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date_updated_product',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 20, 56, 14, 653165, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='date_created_stock',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 20, 56, 32, 274936, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='date_updated_stock',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 20, 56, 37, 429491, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

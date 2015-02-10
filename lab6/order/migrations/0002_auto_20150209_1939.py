# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_created_customer',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 19, 39, 7, 63036, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='date_updated_customer',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 19, 39, 23, 907152, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

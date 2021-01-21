# Generated by Django 3.1.3 on 2021-01-21 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz_payment', '0023_auto_20210103_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='product_profile',
            field=models.CharField(choices=[('airline-tickets', 'airline-tickets'), ('physical-goods', 'physical-goods'), ('non-physical-goods', 'non-physical-goods'), ('general', 'general'), ('telecom-vertical', 'telecom-vertical'), ('travel-vertical', 'travel-vertical')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='shipping_method',
            field=models.CharField(choices=[('TRUCK', 'TRUCK'), ('AIR', 'AIR'), ('SHIP', 'SHIP'), ('NO', 'NO'), ('YES', 'YES'), ('COURIER', 'COURIER'), ('OTHERS', 'OTHERS')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='tran_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
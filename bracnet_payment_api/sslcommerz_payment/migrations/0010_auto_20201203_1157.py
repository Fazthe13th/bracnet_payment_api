# Generated by Django 3.1.3 on 2020-12-03 11:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz_payment', '0009_auto_20201203_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='product_profile',
            field=models.CharField(choices=[('airline-tickets', 'airline-tickets'), ('general', 'general'), ('telecom-vertical', 'telecom-vertical'), ('non-physical-goods', 'non-physical-goods'), ('travel-vertical', 'travel-vertical'), ('physical-goods', 'physical-goods')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='shipping_method',
            field=models.CharField(choices=[('SHIP', 'SHIP'), ('AIR', 'AIR'), ('TRUCK', 'TRUCK'), ('OTHERS', 'OTHERS'), ('COURIER', 'COURIER'), ('NO', 'NO'), ('YES', 'YES')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_brand',
            field=models.CharField(choices=[('VISA', 'VISA'), ('IB', 'IB'), ('MASTER', 'MASTER'), ('MOBILE BANKING', 'MOBILE BANKING'), ('AMEX', 'AMEX')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='currency_rate',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='tran_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 11, 57, 43, 577339, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='validated_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 11, 57, 43, 577636, tzinfo=utc)),
        ),
    ]

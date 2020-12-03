# Generated by Django 3.1.3 on 2020-12-03 11:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz_payment', '0008_auto_20201203_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='product_profile',
            field=models.CharField(choices=[('airline-tickets', 'airline-tickets'), ('travel-vertical', 'travel-vertical'), ('telecom-vertical', 'telecom-vertical'), ('non-physical-goods', 'non-physical-goods'), ('general', 'general'), ('physical-goods', 'physical-goods')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='shipping_method',
            field=models.CharField(choices=[('COURIER', 'COURIER'), ('YES', 'YES'), ('NO', 'NO'), ('AIR', 'AIR'), ('OTHERS', 'OTHERS'), ('TRUCK', 'TRUCK'), ('SHIP', 'SHIP')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='account_details',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_brand',
            field=models.CharField(choices=[('AMEX', 'AMEX'), ('MOBILE BANKING', 'MOBILE BANKING'), ('VISA', 'VISA'), ('MASTER', 'MASTER'), ('IB', 'IB')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='emi_issuer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='risk_level',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='risk_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='tran_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 11, 45, 23, 523184, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='validated_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 11, 45, 23, 523475, tzinfo=utc)),
        ),
    ]

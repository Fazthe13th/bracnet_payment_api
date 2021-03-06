# Generated by Django 3.1.3 on 2020-12-03 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz_payment', '0010_auto_20201203_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='product_profile',
            field=models.CharField(choices=[('general', 'general'), ('travel-vertical', 'travel-vertical'), ('airline-tickets', 'airline-tickets'), ('non-physical-goods', 'non-physical-goods'), ('physical-goods', 'physical-goods'), ('telecom-vertical', 'telecom-vertical')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='shipping_method',
            field=models.CharField(choices=[('AIR', 'AIR'), ('YES', 'YES'), ('TRUCK', 'TRUCK'), ('OTHERS', 'OTHERS'), ('SHIP', 'SHIP'), ('COURIER', 'COURIER'), ('NO', 'NO')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='account_details',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='bank_tran_id',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_brand',
            field=models.CharField(choices=[('AMEX', 'AMEX'), ('VISA', 'VISA'), ('MASTER', 'MASTER'), ('IB', 'IB'), ('MOBILE BANKING', 'MOBILE BANKING')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_issuer',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_no',
            field=models.CharField(default=None, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_ref_id',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_type',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='currency',
            field=models.CharField(default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='currency_rate',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='discount_remarks',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='emi_issuer',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='risk_level',
            field=models.CharField(default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='risk_title',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='status',
            field=models.CharField(choices=[('INVALID_TRANSACTION', 'INVALID_TRANSACTION'), ('VALIDATED', 'VALIDATED')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='tran_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 12, 2, 12, 438848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='validated_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 12, 2, 12, 439135, tzinfo=utc)),
        ),
    ]

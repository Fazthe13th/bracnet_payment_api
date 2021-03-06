# Generated by Django 3.1.3 on 2020-12-03 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz_payment', '0006_auto_20201203_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='store_id',
        ),
        migrations.RemoveField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='verify_key',
        ),
        migrations.RemoveField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='verify_sign',
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='account_details',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='base_fair',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_ref_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='currency_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='discount_remarks',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='emi_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='emi_description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='emi_instalment',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='emi_issuer',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='risk_level',
            field=models.CharField(default=None, max_length=3),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='risk_title',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='validated_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 11, 39, 28, 155501, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='product_profile',
            field=models.CharField(choices=[('non-physical-goods', 'non-physical-goods'), ('physical-goods', 'physical-goods'), ('airline-tickets', 'airline-tickets'), ('general', 'general'), ('telecom-vertical', 'telecom-vertical'), ('travel-vertical', 'travel-vertical')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='shipping_method',
            field=models.CharField(choices=[('TRUCK', 'TRUCK'), ('OTHERS', 'OTHERS'), ('AIR', 'AIR'), ('SHIP', 'SHIP'), ('NO', 'NO'), ('COURIER', 'COURIER'), ('YES', 'YES')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_brand',
            field=models.CharField(choices=[('AMEX', 'AMEX'), ('MASTER', 'MASTER'), ('VISA', 'VISA'), ('MOBILE BANKING', 'MOBILE BANKING'), ('IB', 'IB')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_issuer',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_issuer_country',
            field=models.CharField(default='Bangladesh', max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_issuer_country_code',
            field=models.CharField(default='BD', max_length=2),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='card_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='currency',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='currency_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='currency_type',
            field=models.CharField(default='BDT', max_length=3),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='status',
            field=models.CharField(choices=[('INVALID_TRANSACTION', 'INVALID_TRANSACTION'), ('VALIDATED', 'VALIDATED')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='tran_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 11, 39, 28, 155151, tzinfo=utc)),
        ),
    ]

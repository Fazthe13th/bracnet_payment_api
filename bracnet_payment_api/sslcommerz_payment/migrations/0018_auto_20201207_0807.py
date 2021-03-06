# Generated by Django 3.1.3 on 2020-12-07 08:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz_payment', '0017_auto_20201207_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='product_profile',
            field=models.CharField(choices=[('telecom-vertical', 'telecom-vertical'), ('physical-goods', 'physical-goods'), ('travel-vertical', 'travel-vertical'), ('airline-tickets', 'airline-tickets'), ('general', 'general'), ('non-physical-goods', 'non-physical-goods')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='shipping_method',
            field=models.CharField(choices=[('COURIER', 'COURIER'), ('AIR', 'AIR'), ('TRUCK', 'TRUCK'), ('SHIP', 'SHIP'), ('NO', 'NO'), ('OTHERS', 'OTHERS'), ('YES', 'YES')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='tran_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 8, 7, 22, 254475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentvalidatemodel',
            name='validated_on',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]

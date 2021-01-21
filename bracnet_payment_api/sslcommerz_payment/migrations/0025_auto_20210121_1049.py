# Generated by Django 3.1.3 on 2021-01-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz_payment', '0024_auto_20210121_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='product_profile',
            field=models.CharField(choices=[('physical-goods', 'physical-goods'), ('travel-vertical', 'travel-vertical'), ('non-physical-goods', 'non-physical-goods'), ('general', 'general'), ('telecom-vertical', 'telecom-vertical'), ('airline-tickets', 'airline-tickets')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitializationmodel',
            name='shipping_method',
            field=models.CharField(choices=[('YES', 'YES'), ('AIR', 'AIR'), ('NO', 'NO'), ('SHIP', 'SHIP'), ('OTHERS', 'OTHERS'), ('TRUCK', 'TRUCK'), ('COURIER', 'COURIER')], max_length=20),
        ),
    ]

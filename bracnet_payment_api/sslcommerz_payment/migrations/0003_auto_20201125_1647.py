# Generated by Django 3.1.3 on 2020-11-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz_payment', '0002_auto_20201125_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='sslcommerzpaymentinitialization',
            name='failed_reason',
            field=models.TextField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='sslcommerzpaymentinitialization',
            name='status',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitialization',
            name='product_profile',
            field=models.CharField(choices=[('general', 'general'), ('travel-vertical', 'travel-vertical'), ('non-physical-goods', 'non-physical-goods'), ('telecom-vertical', 'telecom-vertical'), ('airline-tickets', 'airline-tickets'), ('physical-goods', 'physical-goods')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitialization',
            name='shipping_method',
            field=models.CharField(choices=[('COURIER', 'COURIER'), ('SHIP', 'SHIP'), ('NO', 'NO'), ('AIR', 'AIR'), ('YES', 'YES'), ('OTHERS', 'OTHERS'), ('TRUCK', 'TRUCK')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sslcommerzpaymentinitialization',
            name='tran_id',
            field=models.UUIDField(db_index=True, unique=True),
        ),
    ]

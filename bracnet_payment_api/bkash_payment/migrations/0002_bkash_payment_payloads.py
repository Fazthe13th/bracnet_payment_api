# Generated by Django 3.1.3 on 2021-01-21 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bkash_payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bKash_payment_payloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(db_index=True, max_length=100, unique=True)),
                ('transaction_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('payment_from', models.CharField(max_length=20)),
                ('transaction_status', models.CharField(max_length=30)),
                ('transaction_reference', models.CharField(blank=True, max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('currency', models.CharField(max_length=3)),
                ('sns_response', models.JSONField()),
            ],
        ),
    ]
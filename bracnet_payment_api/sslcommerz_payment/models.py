from django.db import models
import uuid
# Create your models here.


class SslcommerzPaymentInitializationModel(models.Model):
    SHIPPING_METHOD_OPTIONS = {
        ('NO', 'NO'),
        ('YES', 'YES'),
        ('AIR', 'AIR'),
        ('COURIER', 'COURIER'),
        ('SHIP', 'SHIP'),
        ('TRUCK', 'TRUCK'),
        ('OTHERS', 'OTHERS')
    }
    PRODUCT_PROFILE = {
        ('general', 'general'),
        ('physical-goods', 'physical-goods'),
        ('non-physical-goods', 'non-physical-goods'),
        ('airline-tickets', 'airline-tickets'),
        ('travel-vertical', 'travel-vertical'),
        ('telecom-vertical', 'telecom-vertical')
    }
    tran_id = models.UUIDField(
        unique=True, db_index=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    emi_option = models.BooleanField(default=False)
    cus_name = models.CharField(max_length=200)
    cus_phone = models.CharField(max_length=20)
    cus_email = models.EmailField(max_length=255)
    cus_add1 = models.TextField(null=True, default=None)
    cus_city = models.CharField(max_length=40, null=True, default=None)
    cus_country = models.CharField(max_length=50, null=True, default=None)
    shipping_method = models.CharField(
        choices=SHIPPING_METHOD_OPTIONS, max_length=20)
    num_of_item = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    product_profile = models.CharField(choices=PRODUCT_PROFILE, max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, default=None)
    failed_reason = models.TextField(max_length=500, default=None)

    def __str__(self):
        return "Transaction id "+str(self.tran_id) + " and Customer name "+str(self.cus_name)


class SslcommerzPaymentValidateModel(models.Model):
    status_choices = ['VALID', 'FAILED', 'CANCELLED', 'UNATTEMPTED', 'EXPIRED']
    card_brand_choices = ['VISA', 'MASTER', 'AMEX', 'IB', 'MOBILE BANKING']
    tran_id = models.UUIDField(unique=True, db_index=True)
    val_id = models.CharField(unique=True, db_index=True, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_type = models.CharField(max_length=255)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(max_length=16)
    bank_tran_id = models.CharField(max_length=255)
    status = models.CharField(choices=status_choices)
    tran_date = models.DateTimeField()
    currency = models.CharField()
    card_issuer = models.CharField(max_length=50)
    card_brand = models.CharField(choices=card_brand_choices)
    card_issuer_country = models.CharField(max_length=50)
    card_issuer_country_code = models.CharField(max_length=2)
    store_id = models.CharField(max_length=50)
    verify_sign = models.CharField(max_length=255)
    verify_key = models.CharField()
    currency_type = models.CharField(max_length=3)
    currency_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Transaction id "+str(self.tran_id) + " has status "+str(self.status)

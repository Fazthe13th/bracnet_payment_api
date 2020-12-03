from django.db import models
from django.utils.timezone import now
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

    class Meta:
        ordering: ['-payment_date']

    def __str__(self):
        return "Transaction id "+str(self.tran_id) + " and Customer name "+str(self.cus_name)


class SslcommerzPaymentValidateModel(models.Model):
    STATUS_CHOICES = {
        ('VALIDATED', 'VALIDATED'), ('INVALID_TRANSACTION', 'INVALID_TRANSACTION')
    }
    CARD_BRAND_CHOICES = {
        ('VISA', 'VISA'), ('MASTER', 'MASTER'), ('AMEX',
                                                 'AMEX'), ('IB', 'IB'), ('MOBILE BANKING', 'MOBILE BANKING')
    }
    tran_id = models.UUIDField(unique=True, db_index=True)
    val_id = models.CharField(unique=True, db_index=True, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    card_type = models.CharField(max_length=255, null=True, default=None)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(max_length=16, null=True, default=None)
    bank_tran_id = models.CharField(max_length=255, null=True, default=None)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=50, null=True, default=None)
    tran_date = models.DateTimeField(default=now())
    currency = models.CharField(max_length=3, null=True, default=None)
    card_issuer = models.CharField(max_length=50, null=True, default=None)
    card_brand = models.CharField(choices=CARD_BRAND_CHOICES, max_length=50)
    card_issuer_country = models.CharField(max_length=50, default='Bangladesh')
    card_issuer_country_code = models.CharField(max_length=2, default='BD')
    currency_type = models.CharField(max_length=3, default='BDT')
    currency_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    currency_rate = models.DecimalField(
        max_digits=10, decimal_places=5, default=0.00)
    base_fair = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    emi_instalment = models.CharField(max_length=3, default=0)
    emi_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    emi_description = models.TextField(default='no description')
    emi_issuer = models.CharField(max_length=100, null=True, default=None)
    risk_title = models.CharField(max_length=50, null=True, default=None)
    risk_level = models.CharField(max_length=3, null=True, default=None)
    validated_on = models.DateTimeField(default=now())
    card_ref_id = models.CharField(max_length=255, null=True, default=None)
    discount_percentage = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=None)
    discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=None)
    discount_remarks = models.TextField(null=True, default=None)

    class Meta:
        ordering: ['-tran_date']

    def __str__(self):
        return "Transaction id "+str(self.tran_id) + " has status "+str(self.status)

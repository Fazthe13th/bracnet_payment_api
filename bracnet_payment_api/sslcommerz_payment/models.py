from django.db import models
import uuid
# Create your models here.


class SslcommerzPaymentInitialization(models.Model):
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

from django.db import models
from datetime import datetime


class bKash_Onboarding(models.Model):
    onbording_res = models.JSONField()

    def __str__(self):
        return "Onboarding json string "+str(self.onbording_res)


class bKash_payment_payloads(models.Model):
    transaction_id = models.CharField(
        db_index=True, unique=True, max_length=100)
    transaction_datetime = models.DateTimeField(default=datetime.now)
    payment_from = models.CharField(max_length=20)
    transaction_status = models.CharField(max_length=30)
    transaction_reference = models.CharField(
        blank=True, max_length=100, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3)
    sns_response = models.JSONField()

    def __str__(self):
        return "bKash payment info for " + str(self.transaction_id)

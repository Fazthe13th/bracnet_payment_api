from rest_framework import serializers
from .models import SslcommerzPaymentInitializationModel, SslcommerzPaymentValidateModel


class SslcommerzPaymentInitializationSerializer(serializers.ModelSerializer):
    tran_id = serializers.UUIDField(read_only=True)

    class Meta:
        model = SslcommerzPaymentInitializationModel
        fields = ['tran_id', 'total_amount', 'currency', 'emi_option', 'cus_name', 'cus_phone', 'cus_email', 'cus_add1',
                  'cus_city', 'cus_country', 'shipping_method', 'num_of_item', 'product_name', 'product_category', 'product_profile']

    def validate(self, attrs):
        return attrs


class SslcommerzIPNSerializer(serializers.Serializer):
    STATUS_CHOICES = {
        ('VALID', 'VALID'), ('FAILED', 'FAILED'), ('CANCELLED',
                                                   'CANCELLED'), ('UNATTEMPTED', 'UNATTEMPTED'), ('EXPIRED', 'EXPIRED')
    }
    CARD_BRAND_CHOICES = {
        ('VISA', 'VISA'), ('MASTER', 'MASTER'), ('AMEX',
                                                 'AMEX'), ('IB', 'IB'), ('MOBILE BANKING', 'MOBILE BANKING')
    }
    tran_id = serializers.UUIDField(read_only=True)
    val_id = serializers.CharField(read_only=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    card_type = serializers.CharField(max_length=255)
    store_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    card_no = serializers.CharField(max_length=16)
    bank_tran_id = serializers.CharField(max_length=255)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    tran_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    currency = serializers.CharField(min_length=3)
    card_issuer = serializers.CharField(max_length=50)
    card_brand = serializers.ChoiceField(choices=CARD_BRAND_CHOICES)
    card_issuer_country = serializers.CharField(max_length=50)
    card_issuer_country_code = serializers.CharField(max_length=2)
    store_id = serializers.CharField(max_length=50)
    verify_sign = serializers.CharField(max_length=255)
    verify_key = serializers.CharField()
    currency_type = serializers.CharField(max_length=3)
    currency_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        fields = ['tran_id', 'val_id', 'amount', 'card_type', 'store_amount', 'card_no', 'bank_tran_id',
                  'status', 'tran_date', 'currency', 'card_issuer', 'card_brand', 'card_issuer_country', 'card_issuer_country_code',
                  'store_id', 'verify_sign', 'verify_key', 'currency_type', 'currency_amount']

    def validate(self, attrs):
        tran_id = attrs.get('tran_id', None)
        status = attrs.get('status', None)
        amount = attrs.get('amount', None)
        currency_type = attrs.get('currency_type', None)
        currency_amount = attrs.get('currency_amount', None)
        session_data = SslcommerzPaymentInitializationModel.objects.filter(
            tran_id=tran_id)
        import pdb
        pdb.set_trace()
        return attrs


class SslcommerzValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SslcommerzPaymentValidateModel
        fields = ['tran_id', 'val_id', 'amount', 'card_type', 'store_amount', 'card_no', 'bank_tran_id',
                  'status', 'tran_date', 'currency', 'card_issuer', 'card_brand', 'card_issuer_country', 'card_issuer_country_code',
                  'store_id', 'verify_sign', 'verify_key', 'currency_type', 'currency_amount']

    def validate(self, attrs):
        return attrs

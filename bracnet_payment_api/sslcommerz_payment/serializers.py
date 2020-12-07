from rest_framework import serializers
from .models import SslcommerzPaymentInitializationModel, SslcommerzPaymentValidateModel
from django.shortcuts import get_object_or_404


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
    tran_id = serializers.UUIDField()
    val_id = serializers.CharField(
        required=False, allow_blank=True)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    card_type = serializers.CharField(
        max_length=255,   required=False, allow_blank=True)
    store_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False)
    card_no = serializers.CharField(
        max_length=16,   required=False, allow_blank=True)
    bank_tran_id = serializers.CharField(max_length=255)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    tran_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    currency = serializers.CharField(min_length=3)
    card_issuer = serializers.CharField(
        max_length=50,   required=False, allow_blank=True)
    card_brand = serializers.ChoiceField(
        choices=CARD_BRAND_CHOICES,   required=False, allow_blank=True)
    card_issuer_country = serializers.CharField(
        max_length=50,   required=False, allow_blank=True)
    card_issuer_country_code = serializers.CharField(
        max_length=2,   required=False, allow_blank=True)
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
        amount = attrs.get('amount', None)
        currency_type = attrs.get('currency_type', None)
        # currency_amount = attrs.get('currency_amount', None)
        if not tran_id:
            raise serializers.ValidationError('Transaction ID is empty')
        if not amount:
            raise serializers.ValidationError('Amount field is empty')
        if not currency_type:
            raise serializers.ValidationError('Currency Type field is empty')
        # if not currency_amount:
        #     raise serializers.ValidationError('Currency amount field is empty')
        session_data = get_object_or_404(
            SslcommerzPaymentInitializationModel, tran_id=tran_id)
        if not session_data:
            raise serializers.ValidationError(
                'SSLCommerz session was never created for this request')
        if session_data.total_amount != amount:
            raise serializers.ValidationError(
                'Amount does not match with session creation amount')
        if session_data.currency != currency_type:
            raise serializers.ValidationError(
                'Currency type did not match with session currency type')
        return attrs


class SslcommerzValidationSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(
        max_digits=10, decimal_places=2)
    card_type = serializers.CharField(required=False, allow_blank=True)
    card_no = serializers.CharField(required=False, allow_blank=True)
    bank_tran_id = serializers.CharField(required=False, allow_blank=True)
    tran_date = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", input_formats=['%Y-%m-%d %H:%M:%S', ])
    validated_on = serializers.DateTimeField(
        allow_null=True, required=False)
    val_id = serializers.CharField(required=False, allow_blank=True)
    card_issuer = serializers.CharField(required=False, allow_blank=True)
    card_brand = serializers.CharField(required=False, allow_blank=True)
    card_issuer_country = serializers.CharField(
        required=False, allow_blank=True)
    card_issuer_country_code = serializers.CharField(
        required=False, allow_blank=True)
    emi_description = serializers.CharField(required=False, allow_blank=True)
    emi_issuer = serializers.CharField(required=False, allow_blank=True)
    discount_remarks = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = SslcommerzPaymentValidateModel
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    # 'tran_id'
    # 'val_id'
    # 'amount'
    # 'card_type'
    # 'store_amount'
    # 'card_no'
    # 'bank_tran_id'
    # 'status'
    # 'tran_date'
    # 'currency'
    # 'card_issuer'
    # 'card_brand'
    # 'card_issuer_country'
    # 'card_issuer_country_code'
    # 'currency_type'
    # 'currency_amount'
    # 'currency_rate'
    # 'base_fair'
    # 'emi_instalment'
    # 'emi_amount'
    # 'emi_description'
    # emi_issuer
    # account_details
    # risk_title
    # risk_level
    # validated_on
    # card_ref_id
    # discount_percentage
    # discount_amount
    # discount_remarks

    # {"amount": "1500.00",
    #  "bank_tran_id": "2012061745429BE4sFxEgnvawsk",
    #   "base_fair": "0.00",
    #    "card_brand": ",
    #     "card_issuer": ",
    #      "card_issuer_country": ",
    #       "card_issuer_country_code": ",
    #        "card_no": ",
    #         "card_sub_brand": "Classic",
    #          "card_type": ",
    #           "currency": "BDT",
    #            "currency_amount": "1500.00",
    #             "currency_rate": "1.0000",
    #              "currency_type": "BDT",
    #               "error": "Do not honor",
    #                "status": "FAILED",
    #                 "store_id": "bracn5f9fee32c615c",
    #                  "tran_date": "2020-12-06 17:45:20",
    #                   "tran_id": "a72c8151-2f64-4c04-a149-ab79d42b3b71",
    #                    "value_a": ",
    #                     "value_b": ",
    #                      "value_c": ",
    #                       "value_d": ",
    #                        "verify_sign": "06cf43b331e79f45b07a23aab61861a6",
    #                         "verify_sign_sha2": ["776fc0466c7842ff9cdda06b5b99fd491880fb87ead1f18eef10ba75f5556631",
    #                          "verify_key": ["amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_sub_brand,card_type,currency,currency_amount,currency_rate,currency_type,error,status,store_id,tran_date,tran_id,value_a,value_b,value_c,value_d"}
# {"amount": "1500.00",
#      "bank_tran_id": "2012061745429BE4sFxEgnvawsk",
#       "base_fair": "0.00",
#        "card_brand": "",
#         "card_issuer": "",
#          "card_issuer_country": "",
#           "card_issuer_country_code": "",
#            "card_no": "",
#             "card_sub_brand": "Classic",
#              "card_type": "",
#               "currency": "BDT",
#                "currency_amount": "1500.00",
#                 "currency_rate": "1.0000",
#                  "currency_type": "BDT",
#                   "error": "Do not honor",
#                    "status": "FAILED",
#                     "store_id": "bracn5f9fee32c615c",
#                      "tran_date": "2020-12-06 17:45:20",
#                       "tran_id": "a72c8151-2f64-4c04-a149-ab79d42b3b71",
#                        "value_a": "",
#                         "value_b": "",
#                          "value_c": "",
#                           "value_d": "",
#                            "verify_sign": "06cf43b331e79f45b07a23aab61861a6",
#                             "verify_sign_sha2": "776fc0466c7842ff9cdda06b5b99fd491880fb87ead1f18eef10ba75f5556631",
#                              "verify_key":"amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_sub_brand,card_type,currency,currency_amount,currency_rate,currency_type,error,status,store_id,tran_date,tran_id,value_a,value_b,value_c,value_d"}

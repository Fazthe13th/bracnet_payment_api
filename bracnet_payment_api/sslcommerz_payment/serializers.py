from rest_framework import serializers
from .models import SslcommerzPaymentInitialization


class SslcommerzPaymentInitializationSerializer(serializers.ModelSerializer):
    tran_id = serializers.UUIDField(read_only=True)
    # total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    # currency = serializers.CharField(max_length=3)
    # emi_option = serializers.BooleanField()
    # cus_name = serializers.CharField(max_length=200)
    # cus_phone = serializers.CharField(max_length=20)
    # cus_email = serializers.EmailField(max_length=255)
    # cus_add1 = serializers.CharField(null=True, default=None)
    # cus_city = serializers.CharField(max_length=40, null=True)
    # cus_country = serializers.CharField(max_length=50, null=True)
    # shipping_method = serializers.CharField(max_length=20)
    # num_of_item = serializers.IntegerField()
    # product_name = serializers.CharField(max_length=50)
    # product_category = serializers.CharField(max_length=50)
    # product_profile = serializers.CharField(max_length=50)

    class Meta:
        model = SslcommerzPaymentInitialization
        fields = ['tran_id', 'total_amount', 'currency', 'emi_option', 'cus_name', 'cus_phone', 'cus_email', 'cus_add1',
                  'cus_city', 'cus_country', 'shipping_method', 'num_of_item', 'product_name', 'product_category', 'product_profile']

    def validate(self, attrs):
        return attrs

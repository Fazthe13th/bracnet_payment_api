from rest_framework import serializers
from .models import bKash_payment_payloads
from .models import bKash_Onboarding


class bkashOnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = bKash_Onboarding
        fields = '__all__'

    def validate(self, attrs):
        return attrs


class bkashWebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = bKash_payment_payloads
        fields = '__all__'

    def validate(self, attrs):
        trans_id = attrs.get('transaction_id', None)
        sent_from = attrs.get('payment_from', None)
        if not trans_id:
            raise serializers.ValidationError(
                "Transaction id should not be null")
        if not sent_from:
            raise serializers.ValidationError(
                "sender phone number should not be null")
        return attrs

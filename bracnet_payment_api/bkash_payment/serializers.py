from rest_framework import serializers
from .models import bKash_Onboarding


class bkashOnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = bKash_Onboarding
        fields = '__all__'

    def validate(self, attrs):
        return attrs

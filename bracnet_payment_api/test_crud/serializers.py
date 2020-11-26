from rest_framework import serializers
from .models import TestCRUD


class ExpenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCRUD
        fields = ['date', 'id', 'description', 'amount', 'category']

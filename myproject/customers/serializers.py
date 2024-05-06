# customers/serializers.py
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['email', 'phone_number', 'opt_in_emails', 'opt_in_sms']

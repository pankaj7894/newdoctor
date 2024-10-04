from rest_framework import serializers
from .models import Appointment, Payment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'user', 'listing', 'appointment_date', 'appointment_time', 'status', 'notes', 'amount', 'payment_mode', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'appointment', 'orderid', 'pg', 'amount', 'payment_date', 'payment_remarks', 'transaction_id', 'status']
        read_only_fields = ['id', 'payment_date']
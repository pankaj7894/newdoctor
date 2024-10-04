from django.db import models
import uuid
from django.conf import settings
from listing.models import Listing

# Create your models here.
class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    notes = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_mode = models.CharField(max_length=20, blank=True, null=True, choices=[('online', 'Online'), ('offline', 'Offline')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment with {self.listing} on {self.appointment_date}"
    


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='payment')
    orderid = models.CharField(max_length=50, blank=True, null=True, unique=True)
    pg = models.CharField(max_length=50, blank=True, null=True, choices=[('razorpay', 'Razorpay'), ('paytm', 'Paytm'),('phonepe', 'PhonePe')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_remarks = models.CharField(max_length=255, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status_choices = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    

    def __str__(self):
        return f"Payment for {self.appointment} - {self.amount}"

from rest_framework import serializers
from .models import Listing, Availability, Unavailability, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'  
        read_only_fields = ['created_at', 'updated_at']  

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['id', 'listing', 'day', 'start_time', 'end_time', 'start_time2', 'end_time2', 'start_time3', 'end_time3', 'slot_time', 'max_in_slot', 'max_in_day', 'status']


class UnavailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Unavailability
        fields = ['id', 'listing', 'dateofunavailability', 'allday', 'start_time', 'end_time', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'listing', 'rating', 'comment', 'created_at', 'updated_at', 'status', 'user']
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from rest_framework import generics
from .serializers import ListingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.mixins import UpdateModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Availability, Unavailability, Review, Listing
from .serializers import (
    AvailabilitySerializer,
    UnavailabilitySerializer,
    ReviewSerializer
)
user = get_user_model()


class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        # Set the user to the logged-in user during creation
        serializer.save(user=self.request.user)

class ListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView, UpdateModelMixin):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        # Print the request headers to console or log
        print("Request Headers:", request.headers)
        
        # Call the parent class's get method
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Listing.objects.filter(user=self.request.user)
        else:
            return Listing.objects.none()

    def update(self, request, *args, **kwargs):
        # Block PUT requests explicitly
        if request.method == 'PUT':
            self.http_method_not_allowed(request, *args, **kwargs)
        return super().partial_update(request, *args, **kwargs)  # Ensuring partial_update is used

    def get_allowed_methods(self):
        allowed_methods = super().get_allowed_methods()
        # Remove PUT from the allowed methods list
        if 'PUT' in allowed_methods:
            allowed_methods.remove('PUT')
        return allowed_methods
    
# Availability Views
class AvailabilityListCreateView(generics.ListCreateAPIView):
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        listing = Listing.objects.get(pk=self.kwargs['listing_id'])
        serializer.save(listing=listing)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Availability.objects.filter(listing_id=self.kwargs['listing_id'])
        else:
            return Availability.objects.none()

class AvailabilityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView, UpdateModelMixin):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def update(self, request, *args, **kwargs):
        # Block PUT requests explicitly
        if request.method == 'PUT':
            self.http_method_not_allowed(request, *args, **kwargs)
        return super().partial_update(request, *args, **kwargs)  # Ensuring partial_update is used

    def get_allowed_methods(self):
        allowed_methods = super().get_allowed_methods()
        # Remove PUT from the allowed methods list
        if 'PUT' in allowed_methods:
            allowed_methods.remove('PUT')
        return allowed_methods   

# Unavailability Views
class UnavailabilityListCreateView(generics.ListCreateAPIView):
    serializer_class = UnavailabilitySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Unavailability.objects.filter(listing_id=self.kwargs['listing_id'])
        else:
            return Unavailability.objects.none()

    def perform_create(self, serializer):
        listing = Listing.objects.get(pk=self.kwargs['listing_id'])
        serializer.save(listing=listing)

class UnavailabilityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView, UpdateModelMixin):
    queryset = Unavailability.objects.all()
    serializer_class = UnavailabilitySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def update(self, request, *args, **kwargs):
        # Block PUT requests explicitly
        if request.method == 'PUT':
            self.http_method_not_allowed(request, *args, **kwargs)
        return super().partial_update(request, *args, **kwargs)  # Ensuring partial_update is used

    def get_allowed_methods(self):
        allowed_methods = super().get_allowed_methods()
        # Remove PUT from the allowed methods list
        if 'PUT' in allowed_methods:
            allowed_methods.remove('PUT')
        return allowed_methods
    
# Review Views
class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Review.objects.filter(listing_id=self.kwargs['listing_id'])
        else:
            return Review.objects.none()


    def perform_create(self, serializer):
        listing = Listing.objects.get(pk=self.kwargs['listing_id'])
        serializer.save(listing=listing)

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView, UpdateModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def update(self, request, *args, **kwargs):
        # Block PUT requests explicitly
        if request.method == 'PUT':
            self.http_method_not_allowed(request, *args, **kwargs)
        return super().partial_update(request, *args, **kwargs)  # Ensuring partial_update is used

    def get_allowed_methods(self):
        allowed_methods = super().get_allowed_methods()
        # Remove PUT from the allowed methods list
        if 'PUT' in allowed_methods:
            allowed_methods.remove('PUT')
        return allowed_methods
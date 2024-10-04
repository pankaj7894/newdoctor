from django.urls import path
from .views import (
    ListingListCreateView, 
    ListingRetrieveUpdateDestroyView,
    AvailabilityListCreateView,
    AvailabilityRetrieveUpdateDestroyView,
    UnavailabilityListCreateView,
    UnavailabilityRetrieveUpdateDestroyView,
    ReviewListCreateView,
    ReviewRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Listings
    path('', ListingListCreateView.as_view(), name='listing-list-create'),
    path('record/<int:pk>/', ListingRetrieveUpdateDestroyView.as_view(), name='listing-detail-update-delete'),

    # Availability
    path('availabilities/<int:listing_id>/', AvailabilityListCreateView.as_view(), name='availability-list-create'),
    path('availabilities/<int:pk>/', AvailabilityRetrieveUpdateDestroyView.as_view(), name='availability-detail-update-delete'),

    # Unavailability
    path('unavailabilities/<int:listing_id>/', UnavailabilityListCreateView.as_view(), name='unavailability-list-create'),
    path('unavailabilities/<int:pk>/', UnavailabilityRetrieveUpdateDestroyView.as_view(), name='unavailability-detail-update-delete'),

    # Reviews
    path('reviews/<int:listing_id>/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-update-delete'),
]
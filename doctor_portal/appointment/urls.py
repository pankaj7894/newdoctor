from django.urls import path
from .views import AppointmentListCreateView, AppointmentRetrieveUpdateDestroyView, PaymentListCreateView, PaymentRetrieveUpdateDestroyView

urlpatterns = [
    path('', AppointmentListCreateView.as_view(), name='appointment-list-create'),  # For listing and creating appointments
    path('<uuid:id>/', AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail-update-delete'),  # For appointment detail, update, and delete by UUID
    path('payments', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('<uuid:id>/payments', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail-update-delete'),
]

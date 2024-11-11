from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from configurations.views import CustomUserListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
    ),
    public=True,  # Set to True for public access
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/users/', CustomUserListView.as_view(), name='users'),
    path('api/listing/', include('listing.urls')),
    path('api/appointments/', include('appointment.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



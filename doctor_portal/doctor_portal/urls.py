from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from configurations.views import CustomUserListView

schema_view = get_schema_view(
    openapi.Info(
        title="Doctor Portal API",
        default_version='v1',
        description="API documentation for the Doctor Portal",
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/users/', CustomUserListView.as_view(), name='users'),
    path('api/listing/', include('listing.urls')),
    path('api/appointments/', include('appointment.urls')),
]



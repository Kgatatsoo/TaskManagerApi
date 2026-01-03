from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskmanagerapp.urls')),  # Include app URLs
    path('auth/', include('rest_framework.urls')),  # DRF login/logout
]

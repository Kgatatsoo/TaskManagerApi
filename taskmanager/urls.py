from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  # this is fine, but check spelling/capitalization
    path('api/', include('taskmanagerapp.urls')),
]
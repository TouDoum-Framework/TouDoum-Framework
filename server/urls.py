# server URL Configuration

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('server.api.urls')),
    path('panel/', include('server.panel.urls')),
    path('', include('server.authentication.urls')),
    path('admin/', admin.site.urls),
]

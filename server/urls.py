# server URL Configuration

from django.contrib import admin
from django.db import ProgrammingError
from django.urls import path, include

urlpatterns = [
    path('api/', include('server.api.urls')),
    path('panel/', include('server.panel.urls')),
    path('cluster/', include('server.cluster.urls')),
    path('modules/', include('server.modules.urls')),
    path('', include('server.authentication.urls')),
    path('admin/', admin.site.urls),
]

try:
    from server.modules.apps import syncDB
    syncDB()
    print("Module Sync OK")
except ProgrammingError:
    print("Module Sync Skipped DB not ready")

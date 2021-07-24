# server URL Configuration

from django.contrib import admin
from django.db import ProgrammingError
from django.urls import path, include

urlpatterns = [
    path('', include('server.panel.urls')),
    path('api/', include('server.api.urls')),
    path('cluster/', include('server.cluster.urls')),
    path('modules/', include('server.modules.urls')),
    path('admin/', admin.site.urls),
]

try:
    from server.modules.apps import syncDB
    syncDB()
    print("Module Sync OK")
except ProgrammingError:
    print("Module Sync Skipped DB not ready")

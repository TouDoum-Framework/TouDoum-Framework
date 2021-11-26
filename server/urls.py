# server URL Configuration

from django.contrib import admin
from django.db import ProgrammingError
from django.urls import path, include

urlpatterns = [
    path('', include('server.panel.urls')),
    path('api/', include('server.api.urls')),
    path('cluster/', include('server.cluster.urls')),
    path('modules/', include('server.modules.urls')),
    path('admin/', admin.site.urls)
]

try:
    print("Init sys data")
    from server.api.apps import register_token_from_env
    from server.modules.apps import sync_db

    print("Loading token on DB ...")
    register_token_from_env()
    print("Loading token on DB OK")

    print("Module Sync ...")
    sync_db()
    print("Module Sync OK")
except ProgrammingError:
    print("Init sys data Skipped DB not ready")

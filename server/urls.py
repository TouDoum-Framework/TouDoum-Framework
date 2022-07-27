# server URL Configuration

from django.contrib import admin
from django.db import ProgrammingError
from django.urls import path, include

urlpatterns = [
    path('', include('server.panel.urls')),
    path('', include('server.api.urls')),
    path('mq/auth', include('server.mq_auth.urls')),
    path('admin/', admin.site.urls)
]

try:
    from server.modules.apps import sync_modules_db
    print("Module Sync ...")
    sync_modules_db()
    print("Module Sync OK")
except ProgrammingError:
    print("Init sys data Skipped DB not ready")

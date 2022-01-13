from django.contrib import admin

from server.api.models.Config import Config
from server.api.models.Addr import Addr

admin.site.register(Config)
admin.site.register(Addr)

from django.contrib import admin
from server.api.models import *

admin.site.register(Config)
admin.site.register(Worker)
admin.site.register(Addr)
admin.site.register(AddrEvent)
admin.site.register(ScanResult)

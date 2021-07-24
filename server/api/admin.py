from django.contrib import admin

from server.api.models.Token import Token
from server.api.models.models import *

admin.site.register(Config)
admin.site.register(Worker)
admin.site.register(Addr)
admin.site.register(Token)

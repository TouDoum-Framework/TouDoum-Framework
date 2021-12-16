from django.urls import path, include
from rest_framework import routers

from server.api.views.BrowsableApi import browsable_API
from server.api.views.AddrViewSet import AddrViewSet
from server.api.views.ConfigViewSet import ConfigViewSet
from server.api.views.ModuleViewSet import ModuleViewSet
from server.modules.apps import get_urls

router = routers.DefaultRouter()

router.register(r'addr', AddrViewSet)
router.register(r'config', ConfigViewSet)
router.register(r'module', ModuleViewSet)

# /api
urlpatterns = [
    path('api', browsable_API, name="browsable_api"),
    path('api/', include(router.urls))
] + get_urls("api")

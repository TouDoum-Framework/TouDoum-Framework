from importlib import import_module

from django.urls import path, include
from rest_framework import routers

from server.api.views.BrowsableApi import browsable_api
from server.api.views.ConfigViewSet import ConfigViewSet
from server.api.views.ModuleViewSet import ModuleViewSet
from server.api.views.ModuleFileViewSet import ModuleFileViewSet
from server.modules.apps import get_api_router_endpoint

main_router = routers.DefaultRouter()

main_router.register(r'config', ConfigViewSet)
main_router.register(r'module', ModuleViewSet)
main_router.register(r'file', ModuleFileViewSet)

# get router of each module and extend main router
for mod_name, subrouter_import_path in get_api_router_endpoint().items():
    mod = import_module(subrouter_import_path)
    main_router.registry.extend(mod.router.registry)

# /api
urlpatterns = [
    path('api', browsable_api, name="browsable_api"),
    path('api/', include(main_router.urls))
]

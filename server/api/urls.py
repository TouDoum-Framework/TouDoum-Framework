from django.urls import path
from server.api import views
from server.modules.apps import get_urls

# /api
urlpatterns = [
    path('v1/worker', views.worker),
    path('v1/addr', views.addr),
    path('discovery', views.modules_discovery),
    path('<str:module>/discovery', views.module_discovery_by_name)
] + get_urls("api")

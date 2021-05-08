from django.urls import path
from server.api import views
from server.modules import ModuleManager

# /api
urlpatterns = [
    path('v1/worker', views.worker),
    path('v1/addr', views.addr),
    path('discovery', views.modules_discovery)
] + ModuleManager.get_urls("api")

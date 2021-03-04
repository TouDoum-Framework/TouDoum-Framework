from django.urls import path, include
from server.api import views

# /api
urlpatterns = [
    path('', views.index),
    path('v1/worker', views.worker),
    path('v1/config', views.config),
    path('v1/config', views.config),
    path('v1/config/<str:plugin>', views.config_get_plugin),
    path('v1/addr', views.addr)
]

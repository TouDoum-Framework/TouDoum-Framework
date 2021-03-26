from django.urls import path
from server.api import views

# /api
urlpatterns = [
    path('v1/worker', views.worker),
    path('v1/config/<str:plugin>', views.config_get_plugin),
    path('v1/addr', views.addr)
]

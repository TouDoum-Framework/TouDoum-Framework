from django.urls import path

from server.modules.apps import get_urls

urlpatterns = [] + get_urls("panel")

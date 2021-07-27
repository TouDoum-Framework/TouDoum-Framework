from django.urls import path, include
from rest_framework import routers

from server.api import views
from server.api import next
from server.modules.apps import get_urls

router = routers.DefaultRouter()
router.register(r'users', next.UserViewSet)
router.register(r'addr', next.AddrViewSet)

# /api
urlpatterns = [
    path('register', views.register),
    path('addr', views.addr),
    path('next', next.nextBrowsableAPI, name="browsable_api"),
    path('next/', include(router.urls))
] + get_urls("api")

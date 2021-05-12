from django.urls import path

from server.modules.apps import get_urls
from server.panel import views_base
from server.panel.views import addr as addr_views

urlpatterns = [
    path('', views_base.index, name='panel_index'),
    path('addr', addr_views.addr, name='panel_addr'),
    path('addr/<str:ip>', addr_views.edit, name='panel_addr_edit'),
] + get_urls("panel")

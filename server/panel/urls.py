# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.urls import path, re_path
from server.panel import views_base
from server.panel.views import addr as addr_views

urlpatterns = [

    path('', views_base.index, name='panel_index'),

    path('addr', addr_views.addr, name='panel_addr'),
    path('addr/<str:ip>', addr_views.edit, name='panel_addr_edit'),

    # Matches any html file
    re_path(r'^.*\.*', views_base.old_pages, name='pages'),

]

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.urls import path, re_path
from server.panel import views

urlpatterns = [

    path('', views.index, name='panel_index'),
    path('addr', views.addr, name="panel_addr"),

    # Matches any html file
    re_path(r'^.*\.*', views.old_pages, name='pages'),

]

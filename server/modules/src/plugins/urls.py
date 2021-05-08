from django.urls import path
from server.modules.src.plugins.views import api as api_views

url_api = [
    path('plugins/discovery', api_views.discovery),
    path('plugins/<str:plugin>', api_views.config_get_plugin)
]
url_panel = []

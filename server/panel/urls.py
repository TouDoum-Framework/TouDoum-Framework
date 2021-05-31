from django.urls import path

from server.modules.apps import get_urls
from server.panel.views.login import login_view as login
from server.panel.views.index import index


urlpatterns = [
    path('', login, name="login"),
    path('panel', index, name="index")
] + get_urls("panel")

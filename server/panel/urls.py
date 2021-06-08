from django.urls import path

from server.modules.apps import get_urls
from server.panel.views import auth
from server.panel.views.index import index
from server.panel.views import modules


urlpatterns = [
    path('', auth.login_view, name="login"),
    path('logout', auth.logout_view, name="logout"),
    path('panel', index, name="index"),
    path('panel/modules', modules.index, name="modules_index")
] + get_urls("panel")

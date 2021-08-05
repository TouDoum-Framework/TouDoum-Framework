from django.urls import path

from server.modules.apps import get_urls
from server.panel.views import auth, modules, ipdb, token
from server.panel.views.index import index

urlpatterns = [
    path('', auth.login_view, name="login"),
    path('logout', auth.logout_view, name="logout"),
    path('panel', index, name="index"),
    path('panel/modules', modules.index, name="modules_index"),
    path('panel/ipdb', ipdb.index, name="ipdb_index"),
    path('panel/token', token.index, name="token_index")
]  # + get_urls("panel")

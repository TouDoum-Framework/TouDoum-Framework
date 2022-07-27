from rest_framework import routers

from modules.example.views.AddrViewSet import AddrViewSet

router = routers.DefaultRouter()
router.register(r'addr', AddrViewSet)
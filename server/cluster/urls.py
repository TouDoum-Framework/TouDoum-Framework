from socket import gethostname
from server.cluster.models import Master
from django.core.cache import cache

urlpatterns = []


# register master if not exist on db
def registerMaster() -> Master:
    master = cache.get("master_" + gethostname())
    if not master:
        master = Master.objects.filter(uuid=gethostname()).first()
        if master is None:
            master = Master()
            master.uuid = gethostname()
            master.save()
        cache.set("master_" + gethostname(), master)
    return master

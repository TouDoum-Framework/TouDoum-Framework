from django.urls import path, include

from server.mq_auth.views import user, vhost, resource, topic

urlpatterns = [
    path('user', user, name="mq_auth_user"),
    path('vhost', vhost, name="vmq_auth_host"),
    path('resource', resource, name="mq_auth_resource"),
    path('topic', topic, name="mq_auth_topic")
]
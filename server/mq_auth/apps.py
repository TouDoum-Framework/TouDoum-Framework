from django.apps import AppConfig


# https://github.com/rabbitmq/rabbitmq-server/tree/master/deps/rabbitmq_auth_backend_http
class MqAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.mq_auth'

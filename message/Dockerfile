FROM rabbitmq:3.8-management

RUN rabbitmq-plugins enable rabbitmq_auth_backend_http

COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config
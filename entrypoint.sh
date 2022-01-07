#!/usr/bin/env bash
function wait_tcp() {
    echo "Checking $3 port";
    try=0;
    try_max=5;
    while ! 2> /dev/null /dev/tcp/"$1"/"$2"; do
        if [[ "$try" -gt $try_max ]]; then
            echo "Unable to check port exiting app";
            exit 1;
        fi
        echo "Failed $3 port checking retry on 5s $try/$try_max";
        ((try++));
        sleep 5;
    done;
    echo "$3 port success";
}

if [[ $MODE == "master" ]]; then
    echo "Starting master";
    wait_tcp "$POSTGRES_HOST" "$POSTGRES_PORT" "PostgreSQL";
    python3 manage.py makemigrations;
    python3 manage.py migrate;
    gunicorn --config server/gunicorn-cfg.py server.wsgi;
elif [[ $MODE == "consumer" ]]; then
    echo "Starting celery consumer";
    celery -A client.TouDoumClient worker "$CELERY_EXTRA_ARGS";
else
    echo "Please set node at master or consumer with MODE env var";
    exit;
fi

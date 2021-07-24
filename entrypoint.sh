#!/usr/bin/env bash
MODE=$(printenv MODE)
SQL_HOST=$(printenv POSTGRES_HOST)
SQL_PORT=$(printenv POSTGRES_PORT)

if [[ $MODE == "master" ]]; then
        echo "Starting master";
        echo "Waiting for postgres..."
        while ! nc -z $SQL_HOST $SQL_PORT; do
                sleep 1
        done
        echo "PostgreSQL started"
        python3 manage.py makemigrations;
        python3 manage.py migrate;
        gunicorn --config server/gunicorn-cfg.py server.wsgi;
elif [[ $MODE == "worker" ]]; then
        echo "Starting worker";
        python3 TouDoumClient.py;
else
        echo "Please set node at master or worker with MODE env var";
        exit;
fi

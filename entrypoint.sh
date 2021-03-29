MODE=$(printenv MODE)
SQL_HOST=$(printenv POSTGRES_HOST)
SQL_PORT=$(printenv POSTGRES_PORT)
DJANGO_SUPERUSER_USERNAME=$(printenv DJANGO_SUPERUSER_USERNAME)
DJANGO_SUPERUSER_PASSWORD=$(printenv DJANGO_SUPERUSER_PASSWORD)
DJANGO_SUPERUSER_EMAIL=$(printenv DJANGO_SUPERUSER_EMAIL)

if [ $MODE == "master" ]; then
	echo "Starting master";
	if [ "$DATABASE" = "postgres" ]; then
		echo "Waiting for postgres..."
		while ! nc -z $SQL_HOST $SQL_PORT; do
			sleep 1
		done
		echo "PostgreSQL started"
	fi
	python3 manage.py makemigrations;
	python3 manage.py migrate;
	if [ -n $DJANGO_SUPERUSER_USERNAME ] && [ -n $DJANGO_SUPERUSER_PASSWORD ] && [ -n $DJANGO_SUPERUSER_EMAIL ]; then
		python3 manage.py createsuperuser --no-input
		echo "Created user " $DJANGO_SUPERUSER_USERNAME
	fi
	gunicorn --config server/gunicorn-cfg.py server.wsgi;
elif [ $MODE == "worker" ]; then
	echo "Starting worker";
	python3 TouDoumClient.py;
else
	echo "Please set node at master or worker with MODE env var";
	exit;
fi

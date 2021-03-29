MODE=$(printenv MODE)

if [ $MODE == "master" ]; then
	echo "Starting master";
	python3 manage.py makemigrations;
	python3 manage.py migrate;
	gunicorn --config server/gunicorn-cfg.py server.wsgi;
elif [ $MODE == "worker" ]; then
	echo "Starting worker";
	python3 TouDoumClient.py;
else
	echo "Please set node at master or worker with MODE env var";
	exit;
fi

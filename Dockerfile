FROM python:3.8.5-buster

LABEL MAINTAINER="gabin.lanore@gmail.com"

RUN apt update && apt install nginx -y --no-install-recommends

ENV SECRET_KEY="No_U"
ENV TOKEN="Youwouuuu"
ENV API_URL="http://127.0.0.1:8000/api/v1"
ENV POSTGRES_HOST=127.0.0.1
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=TouDoum
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=pass

EXPOSE 8020
STOPSIGNAL SIGTERM

WORKDIR /app

COPY . /app

RUN mv nginx.default /etc/nginx/sites-available/default
RUN pip3 install -r requirements.txt
RUN chown -R www-data:www-data /app
RUN chmod 755 entrypoint.sh

ENTRYPOINT [ "bash", "entrypoint.sh" ]
FROM python:3.8.5-buster

LABEL MAINTAINER="gabin.lanore@gmail.com"

ENV SECRET_KEY="No_U"
ENV TOKEN="Youwouuuu"
ENV API_URL="http://127.0.0.1:8000/api/v1"
ENV POSTGRES_HOST=127.0.0.1
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=TouDoum
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=pass

EXPOSE 8000
STOPSIGNAL SIGTERM

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "bash", "entrypoint.sh" ]
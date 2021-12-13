FROM python:3.9.5

LABEL MAINTAINER="gabin.lanore@gmail.com"

RUN apt update && apt install netcat -y

ENV SECRET_KEY="No_U"
ENV TOKEN="Youwouuuu"
ENV API_URL="http://127.0.0.1:8000/api/v1"

ENV POSTGRES_HOST="127.0.0.1"
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=TouDoum
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=pass

ENV REDIS_URL="redis://127.0.0.1:6379/1"

EXPOSE 8000
STOPSIGNAL SIGTERM

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "bash", "entrypoint.sh" ]
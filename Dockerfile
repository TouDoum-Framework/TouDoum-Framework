FROM python:3.10

LABEL MAINTAINER="gabin.lanore@gmail.com"

ENV SECRET_KEY="No_U"
ENV TOKEN="Youwouuuu"
ENV API_URL="http://127.0.0.1:8000/api/v1"

ENV POSTGRES_HOST="127.0.0.1"
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=TouDoum
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=pass

ENV REDIS_URL="redis://127.0.0.1:6379/1"

RUN apt update && apt install bash -y && pip install poetry

EXPOSE 8000

# Used for restart gunicorn wiouthout restarting the container
STOPSIGNAL SIGTERM

# Path of all modules are installed for master or worker
VOLUME /app/modules

WORKDIR /app

# Install libs
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

# Copy App and setup init script
COPY . .
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "/bin/bash", "entrypoint.sh" ]
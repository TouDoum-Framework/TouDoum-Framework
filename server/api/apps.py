import django.db.utils
from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'server.api'


def register_token_from_env() -> None:
    from server.api.models.Token import Token
    from os import environ
    token_list = environ.get("TOKEN").split(",")
    for tk in token_list:
        try:
            Token(token=tk).save()
        except django.db.utils.IntegrityError:
            pass

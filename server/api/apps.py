from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'server.api'


def register_token_from_env() -> None:
    from server.api.models.Token import Token
    from os import environ
    token_list = environ.get("TOKEN").split(",")
    for tk_str in token_list:
        tk = Token.objects.filter(token=tk_str).first()
        if tk is None:
            Token(token=tk).save()

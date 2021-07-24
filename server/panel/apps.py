import hashlib

from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'panel'


def get_avatar(email: str):
    return "https://www.gravatar.com/avatar/" + email.lower() + "?d=retro&f=y"

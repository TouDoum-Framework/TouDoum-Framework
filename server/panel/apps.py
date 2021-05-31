import hashlib

from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'panel'


def get_avatar(email: str):
    return "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode("utf8")) + "?d=retro&f=y"

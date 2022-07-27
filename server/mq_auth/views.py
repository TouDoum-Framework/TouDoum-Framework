from django.http import HttpRequest


def user(request: HttpRequest):
    return "allow administrator"


def vhost(request: HttpRequest):
    return "allow"


def resource(request: HttpRequest):
    return "allow"


def topic(request: HttpRequest):
    return "allow"

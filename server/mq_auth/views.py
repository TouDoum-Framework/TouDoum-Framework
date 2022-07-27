from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user(request: HttpRequest):
    return HttpResponse("allow administrator")


@csrf_exempt
def vhost(request: HttpRequest):
    return HttpResponse("allow")


@csrf_exempt
def resource(request: HttpRequest):
    return HttpResponse("allow")


@csrf_exempt
def topic(request: HttpRequest):
    return HttpResponse("allow")

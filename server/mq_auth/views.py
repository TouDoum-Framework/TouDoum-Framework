from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user(request):
    if 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin':
            return HttpResponse("allow administrator")

        if username == 'someuser':
            return HttpResponse("allow")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_superuser:
                return HttpResponse("allow administrator")
            else:
                return HttpResponse("allow management")
    return HttpResponse("deny")


@csrf_exempt
def vhost(request: HttpRequest):
    return HttpResponse("allow")


@csrf_exempt
def resource(request: HttpRequest):
    return HttpResponse("allow")


@csrf_exempt
def topic(request: HttpRequest):
    return HttpResponse("allow")

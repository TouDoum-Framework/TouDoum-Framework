from django.http import JsonResponse, HttpRequest


def test(request: HttpRequest):
    from client.core.tasks import client_exec
    client_exec.delay("example")
    return JsonResponse({}, status=200)

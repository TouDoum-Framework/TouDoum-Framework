from django.http import JsonResponse, HttpRequest


def test(request: HttpRequest):
    return JsonResponse({}, status=200)
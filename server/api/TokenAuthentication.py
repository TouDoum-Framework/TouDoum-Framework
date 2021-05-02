import os
from django.http import JsonResponse, HttpRequest


def error():
    return JsonResponse({"error": "Invalid Authorization Token"}, status=401)


def is_token_valid(request: HttpRequest):
    return request.headers.get('Authorization') == os.environ.get('TOKEN')

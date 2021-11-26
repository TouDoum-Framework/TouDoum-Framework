from django.http import JsonResponse

from server.api.models.Token import check_token


class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if str(request.path).startswith("/api/"):
            if check_token(request.headers.get('Authorization')):
                return response
            else:
                return JsonResponse({"error": "Invalid Authorization Token"}, status=401)
        else:
            return response

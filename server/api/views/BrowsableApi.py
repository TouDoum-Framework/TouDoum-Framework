from django.http import HttpRequest
from django.shortcuts import render


def browsable_api(request: HttpRequest):
    return render(request, 'browsable.html')

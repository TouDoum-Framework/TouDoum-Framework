from django.http import HttpRequest
from django.shortcuts import render


def browsable_API(request: HttpRequest):
    return render(request, 'browsable.html')

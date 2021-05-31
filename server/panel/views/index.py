from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render


@login_required(login_url="/")
def index(request: HttpRequest):
    return render(request, 'panel/index.html')

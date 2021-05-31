from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

from server.panel.apps import get_avatar


@login_required(login_url="/")
def index(request: HttpRequest):
    return render(request, 'panel/index.html', {
        "avatar": get_avatar(request.user.email)
    })

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

from server.api.models.Token import Token
from server.panel.apps import get_avatar
from server.panel.forms.token_add import TokenAddFrom


@login_required(login_url="/")
def index(request: HttpRequest):

    token_add_form = TokenAddFrom(request.POST or None)
    msg = None

    if request.method == "POST":
        if token_add_form.is_valid():
            Token(token=token_add_form.cleaned_data.get("token")).save()

    token_list = Token.objects.all()

    return render(request, 'panel/token/index.html', {
        "avatar": get_avatar(request.user.email),
        "msg": msg,
        "token_add_form": token_add_form,
        "token_list": token_list
    })

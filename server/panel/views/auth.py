from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from server.panel.forms.auth import LoginForm


def login_view(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("index")

    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Form invalid"

    return render(request, 'login.html', {'form': form, 'msg': msg})


def logout_view(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")
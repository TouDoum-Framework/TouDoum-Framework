from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpRequest
from django.shortcuts import render

from server.api.models.Addr import Addr
from server.panel.apps import get_avatar
from server.panel.forms.ip_add import IpAddFrom

import iptools


@login_required(login_url="/")
def index(request: HttpRequest):
    ip_add_form = IpAddFrom(request.POST or None)
    msg = None

    if request.method == "POST":
        if ip_add_form.is_valid():
            ipr = iptools.IpRangeList(ip_add_form.cleaned_data.get("ip_range")).__iter__()
            try:
                while True:
                    addr = Addr()
                    addr.ip = iptools.next(ipr)
                    addr.scan_priority = ip_add_form.cleaned_data.get("rescan_priority")
                    try:
                        addr.save()
                    except IntegrityError:
                        pass
            except StopIteration:
                pass
            msg = "All ip has ben added"
            ip_add_form = IpAddFrom(None)

    return render(request, 'panel/ipdb/index.html', {
        "avatar": get_avatar(request.user.email),
        "msg": msg,
        "ip_add_form": ip_add_form,
    })

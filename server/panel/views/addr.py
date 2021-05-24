from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpRequest
from django.shortcuts import render

import iptools

from server.api.models.models import *
from server.panel.forms.addr import AddAddrForm
from server.panel.views_base import getHeaderData


@login_required(login_url="/")
def addr(request: HttpRequest):
    context = getHeaderData()

    if request.method == "POST":
        form = AddAddrForm(request.POST)
        if form.is_valid():
            IP_LIST = str(form.cleaned_data["ips"])
            priority = form.cleaned_data["priority"]

            try:
                ips = iptools.IpRangeList(IP_LIST)
                ips = ips.__iter__()
                while True:
                    try:
                        ip = iptools.next(ips)

                        newIp = Addr()
                        newIp.ip = ip
                        newIp.rescanPriority = priority

                        newEvent = AddrEvent()
                        newEvent.ip = newIp
                        newEvent.status = "free"

                        try:
                            newIp.save()
                            newEvent.save()
                        except IntegrityError:
                            pass

                    except StopIteration:
                        print("All send to scanner !")
                        break

                context['addr_form'] = AddAddrForm()
                context['success'] = "All ip have ben added"
            except TypeError:
                context['error'] = "IpRangeList Invalid !"
                context['addr_form'] = form

        else:
            context['addr_form'] = form
    else:
        context['addr_form'] = AddAddrForm()
    context['addrs'] = Addr.objects.all().order_by("-lastUpdate")

    return render(request, 'panel/addr/index.html', context)


@login_required(login_url="/")
def edit(request: HttpRequest, ip: str):
    context = getHeaderData()

    addr: Addr = Addr.objects.filter(ip=ip).last()

    context['ip'] = ip

    if addr is None:
        context['error'] = "Ip not fond"
    else:
        context['addr'] = addr

    return render(request, 'panel/addr/edit.html', context)

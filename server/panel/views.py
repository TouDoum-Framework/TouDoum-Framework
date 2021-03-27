# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.template import loader
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django import template

import iptools

from core.manager.PluginManager import PluginManager

from server.api.models import *
from server.panel.forms.addr import AddAddrForm


def getHeaderData() -> dict:
    context = {
        'ip': Addr.objects.all().count(),
        'pluginTotal': len(PluginManager.plugins),
        'resultTotal': ScanResult.objects.all().count(),
    }
    try:
        context['configVer'] = Config.objects.last().pk
    except AttributeError:
        context['configVer'] = None
    return context


@login_required(login_url="/")
def index(request: HttpRequest):
    pm = PluginManager()
    pm.reload()

    context = getHeaderData()
    context['result'] = ScanResult.objects.all().order_by("createdAt")[0:50]

    return render(request, 'panel/index.html', context)


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
def old_pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

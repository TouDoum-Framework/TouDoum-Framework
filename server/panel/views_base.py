# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django import template

from server.core.PluginManager import PluginManager

from server.api.models import *


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

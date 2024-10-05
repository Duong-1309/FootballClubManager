from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from home.models import DoiBong

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def cau_lac_bo(request):
    context = {'segment': 'cau_lac_bo'}
    html_template = loader.get_template('home/cau-lac-bo.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def cau_thu(request):
    context = {'segment': 'cau_thu'}
    html_template = loader.get_template('home/cau-thu.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def huan_luyen_vien(request):
    context = {'segment': 'huan_luyen_vien'}
    html_template = loader.get_template('home/huan-luyen-vien.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def hop_dong(request):
    context = {'segment': 'hop_dong'}
    html_template = loader.get_template('home/hop-dong.html')
    return HttpResponse(html_template.render(context, request))
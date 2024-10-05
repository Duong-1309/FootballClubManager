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
    print(html_template)
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def thongtincauthu(request):

    doi_bong = DoiBong.objects.filter(ten='Bayern').first()
    if doi_bong is not None:
        context = {
            'ma_doi_bong': doi_bong.ma_doi_bong,
            'ten': doi_bong.ten,
            'san_van_dong': doi_bong.san_van_dong,
            'nam_thanh_lap_lap': doi_bong.nam_thanh_lap
        }
    else:
        context = {}

    html_template = loader.get_template('home/thongtincauthu.html')
    return HttpResponse(html_template.render(context, request))
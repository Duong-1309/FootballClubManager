import datetime
from lib2to3.fixes.fix_input import context

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from home.models import DoiBong, HopDong, CauThu, HuanLuyenVien
from django.shortcuts import render, get_object_or_404

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    s_cau_thu = CauThu.objects.count()
    s_hlv = HuanLuyenVien.objects.count()
    s_hop_dong = HopDong.objects.count()
    s_hop_dong_thang_truoc = HopDong.objects.filter(
        ngay_bat_dau__lt=datetime.date.today() - datetime.timedelta(days=7)
    ).count()
    tong_quan = {
        "hop_dong": {
            "so_luong": s_hop_dong,
            "tang": round((s_hop_dong - s_hop_dong_thang_truoc) / s_hop_dong_thang_truoc * 100,
                          2) if s_hop_dong_thang_truoc != 0 else 0
        }
    }
    bieu_do_luong = {
        "labels": ["Cầu thủ", "Huấn luyện viên"],
        "data": [s_cau_thu, s_hlv],
    }
    context['tong_quan'] = tong_quan
    context['bieu_do_luong'] = bieu_do_luong

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def cau_lac_bo(request):
    context = {'segment': 'cau_lac_bo'}
    html_template = loader.get_template('home/cau-lac-bo.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def chi_tiet_cau_lac_bo(request, DoiBong_id):
    clb = get_object_or_404(DoiBong, pk=DoiBong_id)
    ds_huan_luyen_vien = HuanLuyenVien.objects.filter(doi_bong=clb)
    ds_cau_thu = CauThu.objects.filter(doi_bong=clb)

    context = {
        'ten_clb': clb.ten,
        'logo_clb': clb.logo,
        'so_luong_cau_thu': ds_cau_thu.count(),
        'so_luong_huan_luyen_vien': ds_huan_luyen_vien.count(),
        'san_van_dong': clb.san_van_dong,
        'nam_thanh_lap': clb.nam_thanh_lap,
        'ds_huan_luyen_vien': ds_huan_luyen_vien,
        'ds_cau_thu': ds_cau_thu,
    }

    return render(request, 'home/chi-tiet-cau-lac-bo.html', context)
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
    ds_hop_dong = HopDong.objects.all().order_by('ngay_bat_dau')
    context = {
        'segment': 'hop_dong',
        'ds_hop_dong': ds_hop_dong
    }
    html_template = loader.get_template('home/hop-dong.html')
    return HttpResponse(html_template.render(context, request))
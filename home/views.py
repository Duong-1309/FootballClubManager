import datetime
from lib2to3.fixes.fix_input import context

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from home.models import DoiBong, HopDong, CauThu, HuanLuyenVien, ThanhTichDoiBong
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

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
        "hlv": s_hlv,
        "cau_thu": s_cau_thu,
        "hop_dong": {
            "so_luong": s_hop_dong,
            "tang": round((s_hop_dong - s_hop_dong_thang_truoc) / s_hop_dong_thang_truoc * 100,
                          2) if s_hop_dong_thang_truoc != 0 else 0
        }
    }
    s_cau_thu_theo_clb = CauThu.objects.values('doi_bong__ten').annotate(count=Count('doi_bong')).order_by('-count')
    bieu_do_cau_thu_theo_clb = {
        "labels": [item['doi_bong__ten'] for item in s_cau_thu_theo_clb],
        "data": [item['count'] for item in s_cau_thu_theo_clb]
    }
    bieu_do_hlv_theo_clb = HuanLuyenVien.objects.values('doi_bong__ten').annotate(count=Count('doi_bong')).order_by('-count')
    bieu_do_hlv_theo_clb = {
        "labels": [item['doi_bong__ten'] for item in bieu_do_hlv_theo_clb],
        "data": [item['count'] for item in bieu_do_hlv_theo_clb]
    }
    context['tong_quan'] = tong_quan
    context['bieu_do_hlv_theo_clb'] = bieu_do_hlv_theo_clb
    context['bieu_do_cau_thu_theo_clb'] = bieu_do_cau_thu_theo_clb
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
    ds_thanh_tich = ThanhTichDoiBong.objects.filter(doi_bong=clb)
    context = {
        'ten_clb': clb.ten,
        'logo_clb': clb.logo,
        'so_luong_cau_thu': ds_cau_thu.count(),
        'so_luong_huan_luyen_vien': ds_huan_luyen_vien.count(),
        'san_van_dong': clb.san_van_dong,
        'nam_thanh_lap': clb.nam_thanh_lap,
        'ds_huan_luyen_vien': ds_huan_luyen_vien,
        'ds_cau_thu': ds_cau_thu,
        'ds_thanh_tich': ds_thanh_tich,
        'segment': 'chi-tiet-cau-lac-bo'
    }

    return render(request, 'home/chi-tiet-cau-lac-bo.html', context)
@login_required(login_url="/login/")
def cau_thu(request):
    context = {'segment': 'cau_thu'}
    html_template = loader.get_template('home/cau-thu.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def chi_tiet_cau_thu(request, id):
    cau_thu = CauThu.objects.filter(pk=id).first()
    if not cau_thu:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render({}, request))
    hop_dong = HopDong.objects.filter(cau_thu=cau_thu).first()
    context = {
        'segment': 'cau_thu',
        'cau_thu': cau_thu,
        'hop_dong': hop_dong,
        'danh_hieu': cau_thu.danh_hieu.split(",") if cau_thu.danh_hieu else []
    }
    html_template = loader.get_template('home/chi-tiet-cau-thu.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def huan_luyen_vien(request):
    context = {'segment': 'huan_luyen_vien'}
    html_template = loader.get_template('home/huan-luyen-vien.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def chi_tiet_huan_luyen_vien(request, id):
    hlv = HuanLuyenVien.objects.filter(pk=id).first()
    if not hlv:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render({}, request))
    hop_dong = HopDong.objects.filter(huan_luyen_vien=hlv).first()
    context = {
        'segment': 'huan_luyen_vien',
        'hlv': hlv,
        'tuoi': datetime.date.today().year - hlv.ngay_sinh.year if hlv.ngay_sinh else None,
        'hop_dong': hop_dong,
        'danh_hieu': hlv.danh_hieu.split(",") if hlv.danh_hieu else []
    }
    html_template = loader.get_template('home/chi-tiet-huan-luyen-vien.html')
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
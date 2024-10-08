import datetime
from lib2to3.fixes.fix_input import context

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse

from home.models import DoiBong, HopDong, CauThu, HuanLuyenVien, KinhNghiemHuanLuyen
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import CauThu
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
    bieu_do_luong = {
        "labels": ["Cầu thủ", "Huấn luyện viên"],
        "data": [s_cau_thu, s_hlv],
    }
    context['tong_quan'] = tong_quan
    context['bieu_do_luong'] = bieu_do_luong

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def tim_kiem(request):
    q = request.GET.get('q')
    cauthu = CauThu.objects.filter(ten__icontains=q).values('ma_cau_thu', 'ten', 'hinh_anh')[:3]
    huanluyenvien = HuanLuyenVien.objects.filter(ten__icontains=q).values('ma_hlv', 'ten', 'hinh_anh')[:3]
    doi_bong = DoiBong.objects.filter(ten__icontains=q).values('ma_doi_bong', 'ten', 'logo')[:3]
    return JsonResponse({
        'cau_thu': list(cauthu),
        'huan_luyen_vien': list(huanluyenvien),
        'doi_bong': list(doi_bong)
    })

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


def str(e):
    pass


@login_required(login_url="/login/")
def cau_thu(request):
    try:
        # Lấy danh sách cầu thủ và sắp xếp theo tên
        ds_cau_thu = CauThu.objects.all().order_by('ten')

        # Lấy thông tin câu lạc bộ cho mỗi cầu thủ (dựa trên quan hệ ForeignKey)
        ds_cau_thu_with_clb = [
            {
                'ten': cau_thu.ten,
                'ten_clb': cau_thu.doi_bong.ten,  # Lấy tên câu lạc bộ của cầu thủ
                'vi_tri': cau_thu.vi_tri,  # Lấy vị trí của cầu thủ
                'hinh_anh':cau_thu.hinh_anh,
                'bieu_tuong':cau_thu.doi_bong.logo,
                'ma_cau_thu': cau_thu.ma_cau_thu

            }
            for cau_thu in ds_cau_thu
        ]

        context = {
            'ds_cau_thu': ds_cau_thu_with_clb,
            'segment': 'cau_thu',
        }

        # Render template với context đã được truyền vào
        return render(request, 'home/cau-thu.html', context)

    except Exception as e:
        # Để debug dễ dàng hơn, bạn có thể in ra lỗi
        return HttpResponse(f"Đã xảy ra lỗi: {str(e)}")


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
    try:
        # Lấy danh sách cầu thủ và sắp xếp theo tên
        ds_huan_luyen_vien = HuanLuyenVien.objects.all().order_by('ten')

        # Lấy thông tin câu lạc bộ cho mỗi cầu thủ (dựa trên quan hệ ForeignKey)
        ds_huan_luyen_vien_with_clb = [
            {
                'ten': huan_luyen_vien.ten,
                'ten_clb': huan_luyen_vien.doi_bong.ten,  # Lấy tên câu lạc bộ của cầu thủ
                'chuyen_mon': huan_luyen_vien.chuyen_mon,  # Lấy vị trí của hlv
                'hinh_anh':huan_luyen_vien.hinh_anh,
                'bieu_tuong':huan_luyen_vien.doi_bong.logo,
                'ma_huan_luyen_vien':huan_luyen_vien.ma_hlv

            }
            for huan_luyen_vien in ds_huan_luyen_vien
        ]

        context = {
            'ds_huan_luyen_vien': ds_huan_luyen_vien_with_clb,
            'segment': 'huan_luyen_vien',
        }

        # Render template với context đã được truyền vào
        return render(request, 'home/huan-luyen-vien.html', context)

    except Exception as e:
        # Để debug dễ dàng hơn, bạn có thể in ra lỗi
        return HttpResponse(f"Đã xảy ra lỗi: {str(e)}")


@login_required(login_url="/login/")
def chi_tiet_huan_luyen_vien(request, id):
    hlv = HuanLuyenVien.objects.filter(pk=id).first()
    if not hlv:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render({}, request))
    hop_dong = HopDong.objects.filter(huan_luyen_vien=hlv).first()
    kinh_nghiem = KinhNghiemHuanLuyen.objects.filter(huan_luyen_vien=hlv).order_by('-nam_ket_thuc')
    context = {
        'segment': 'huan_luyen_vien',
        'hlv': hlv,
        'tuoi': datetime.date.today().year - hlv.ngay_sinh.year if hlv.ngay_sinh else None,
        'hop_dong': hop_dong,
        'danh_hieu': hlv.danh_hieu.split(",") if hlv.danh_hieu else [],
        'ds_kinh_nghiem': kinh_nghiem
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
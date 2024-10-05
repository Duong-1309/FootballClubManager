from django.db import models

# Create your models here.
class DoiBong(models.Model):
    ma_doi_bong = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    san_van_dong = models.CharField(max_length=100)
    nam_thanh_lap = models.IntegerField()

    class Meta:
        db_table = 'DoiBong'


class ThanhTichDoiBong(models.Model):
    ma_thanh_tich = models.AutoField(primary_key=True)
    doi_bong = models.ForeignKey(DoiBong, on_delete=models.CASCADE)
    ten_thanh_tich = models.CharField(max_length=255)
    nam = models.IntegerField()
    mo_ta = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'ThanhTichDoiBong'


class CauThu(models.Model):
    ma_cau_thu = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    tuoi = models.IntegerField()
    ngay_sinh = models.DateField()
    quoc_tich = models.CharField(max_length=50)
    chieu_cao = models.DecimalField(max_digits=5, decimal_places=2)
    vi_tri = models.CharField(max_length=50)
    so_ao = models.IntegerField()
    danh_hieu = models.TextField(null=True, blank=True)
    doi_bong = models.ForeignKey(DoiBong, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CauThu'

class HuanLuyenVien(models.Model):
    ma_hlv = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    ngay_sinh = models.DateField()
    quoc_tich = models.CharField(max_length=50)
    chieu_cao = models.DecimalField(max_digits=5, decimal_places=2)
    chuyen_mon = models.CharField(max_length=100)
    danh_hieu = models.TextField(null=True, blank=True)
    doi_bong = models.ForeignKey(DoiBong, on_delete=models.CASCADE)

    class Meta:
        db_table = 'HuanLuyenVien'


class KinhNghiemHuanLuyen(models.Model):
    ma_kinh_nghiem = models.AutoField(primary_key=True)
    huan_luyen_vien = models.ForeignKey(HuanLuyenVien, on_delete=models.CASCADE)
    ten_doi_bong = models.CharField(max_length=100)
    nam_bat_dau = models.IntegerField()
    nam_ket_thuc = models.IntegerField(null=True, blank=True)
    thanh_tich = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'KinhNghiemHuanLuyen'

class HopDong(models.Model):
    ma_hop_dong = models.AutoField(primary_key=True)
    cau_thu = models.ForeignKey(CauThu, on_delete=models.CASCADE, null=True, blank=True)
    huan_luyen_vien = models.ForeignKey(HuanLuyenVien, on_delete=models.CASCADE, null=True, blank=True)
    ngay_bat_dau = models.DateField()
    ngay_ket_thuc = models.DateField()
    luong = models.CharField(max_length=20)
    thuong = models.CharField(max_length=20)
    phi_pha_vo_hop_dong = models.CharField(max_length=20)

    class Meta:
        db_table = 'HopDong'





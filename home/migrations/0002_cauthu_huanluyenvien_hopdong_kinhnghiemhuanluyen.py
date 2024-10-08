# Generated by Django 5.1.1 on 2024-10-03 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CauThu',
            fields=[
                ('ma_cau_thu', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('tuoi', models.IntegerField()),
                ('ngay_sinh', models.DateField()),
                ('quoc_tich', models.CharField(max_length=50)),
                ('chieu_cao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vi_tri', models.CharField(max_length=50)),
                ('so_ao', models.IntegerField()),
                ('danh_hieu', models.TextField(blank=True, null=True)),
                ('doi_bong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doibong')),
            ],
            options={
                'db_table': 'CauThu',
            },
        ),
        migrations.CreateModel(
            name='HuanLuyenVien',
            fields=[
                ('ma_hlv', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('ngay_sinh', models.DateField()),
                ('quoc_tich', models.CharField(max_length=50)),
                ('chieu_cao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chuyen_mon', models.CharField(max_length=100)),
                ('danh_hieu', models.TextField(blank=True, null=True)),
                ('doi_bong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doibong')),
            ],
            options={
                'db_table': 'HuanLuyenVien',
            },
        ),
        migrations.CreateModel(
            name='HopDong',
            fields=[
                ('ma_hop_dong', models.AutoField(primary_key=True, serialize=False)),
                ('ngay_bat_dau', models.DateField()),
                ('ngay_ket_thuc', models.DateField()),
                ('luong', models.CharField(max_length=20)),
                ('thuong', models.CharField(max_length=20)),
                ('phi_pha_vo_hop_dong', models.CharField(max_length=20)),
                ('cau_thu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.cauthu')),
                ('huan_luyen_vien', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.huanluyenvien')),
            ],
            options={
                'db_table': 'HopDong',
            },
        ),
        migrations.CreateModel(
            name='KinhNghiemHuanLuyen',
            fields=[
                ('ma_kinh_nghiem', models.AutoField(primary_key=True, serialize=False)),
                ('ten_doi_bong', models.CharField(max_length=100)),
                ('nam_bat_dau', models.IntegerField()),
                ('nam_ket_thuc', models.IntegerField(blank=True, null=True)),
                ('thanh_tich', models.TextField(blank=True, null=True)),
                ('huan_luyen_vien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.huanluyenvien')),
            ],
            options={
                'db_table': 'KinhNghiemHuanLuyen',
            },
        ),
    ]

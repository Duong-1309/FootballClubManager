# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tim-kiem', views.tim_kiem, name='tim_kiem'),
    path('cau-lac-bo/', views.cau_lac_bo, name='cau-lac-bo'),
    path('cau-lac-bo/<int:DoiBong_id>', views.chi_tiet_cau_lac_bo, name='chi-tiet-cau-lac-bo'),
    path('cau-thu/', views.cau_thu, name='cau-thu'),
    path('cau-thu/<int:id>/', views.chi_tiet_cau_thu, name='chi-tiet-cau-thu'),
    path('huan-luyen-vien/', views.huan_luyen_vien, name='huan-luyen-vien'),
    path('huan-luyen-vien/<int:id>/', views.chi_tiet_huan_luyen_vien, name='chi-tiet-huan-luyen-vien'),
    path('hop-dong/', views.hop_dong, name='hop-dong'),
]

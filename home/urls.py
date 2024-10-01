# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
]

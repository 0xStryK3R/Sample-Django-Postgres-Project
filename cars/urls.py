# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 10:27:01 2022

@author: arupb
"""

from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.car_detail, name="car_detail"),

]
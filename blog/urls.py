# -*- coding: utf-8 -*-
__time__ = '2018/5/8 14:46'
__author__ = 'zhw'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
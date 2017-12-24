#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @license : Copyright(C), sanshao90.com
# @Contact : luckylhb90@gmail.com
# @Site    : 
# @Software: PyCharm
# @File    : urls.py
# @Desc    :
# @Author  : sanshao90
# @Time    : 2017/12/24 13:32

from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail')
]

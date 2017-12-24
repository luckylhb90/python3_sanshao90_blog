#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("欢迎访问我的博客首页！")
    body = {'title': 'SanShao Blog', 'welcome': '欢迎访问我的博客首页'}
    return render(request, 'blog/index.html', context=body)

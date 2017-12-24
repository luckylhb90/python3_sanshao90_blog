#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    body = {'title': 'SanShao Blog', 'welcome': '欢迎访问我的博客首页', 'post_list': post_list}
    return render(request, 'blog/index.html', context=body)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})

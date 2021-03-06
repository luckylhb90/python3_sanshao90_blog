#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown
from django.shortcuts import render, get_object_or_404

from .models import Post, Category


# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    body = {'title': 'SanShao Blog', 'welcome': '欢迎访问我的博客首页', 'post_list': post_list}
    return render(request, 'blog/index.html', context=body)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    print(post_list)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

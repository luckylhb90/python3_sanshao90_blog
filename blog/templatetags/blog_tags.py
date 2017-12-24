#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @license : Copyright(C), sanshao90.com
# @Contact : luckylhb90@gmail.com
# @Site    : 
# @Software: PyCharm
# @File    : blog_tags.py
# @Desc    :
# @Author  : sanshao90
# @Time    : 2017/12/24 20:04

from django import template
from ..models import Post, Category

register = template.Library()


@register.simple_tag
def get_recent_posts(pagenum=5):
    return Post.objects.all().order_by('-create_time')[:pagenum]


@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()

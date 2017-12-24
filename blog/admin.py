#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'update_time', 'category', 'create_user']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

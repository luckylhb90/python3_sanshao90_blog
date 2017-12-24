#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
公共字段
'''


class CommonFileld(models.Model):
    # 创建时间
    create_time = models.DateTimeField('创建时间')
    # 修改时间
    update_time = models.DateTimeField('修改时间')
    # 创建人
    create_user = models.OneToOneField('创建人', User)
    # 修改人
    update_user = models.OneToOneField('修改人', User)
    # 备注
    remark = models.CharField('备注', max_length=200, blank=True)

    class Meta:
        abstract = True


class Category(CommonFileld):
    """
        Django 要求模型必须继承 models.Model 类。
        Category 只需要一个简单的分类名 name 就可以了。
        CharField 指定了分类名 name 的数据类型，CharField 是字符型，
        CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
        当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
        Django 内置的全部类型可查看文档：
        https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField('名称', max_length=100)


class Tag(CommonFileld):
    """
        标签 Tag 也比较简单，和 Category 一样。
        再次强调一定要继承 models.Model 类！
    """
    name = models.CharField('名称', max_length=100)


class Post(CommonFileld):
    '''
    文章数据库表
    '''
    # 标题
    title = models.CharField('标题', max_length=80)
    # 标题颜色
    title_color = models.CharField('标题颜色', max_length=20, blank=True)
    # 文章正文
    body = models.TextField('文章正文')
    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField('文章摘要', max_length=200, blank=True)
    # 文章类别
    category = models.OneToOneField('文章类别', Category)
    # 文章标签
    tags = models.ManyToManyField('文章标签', Tag, blank=True)

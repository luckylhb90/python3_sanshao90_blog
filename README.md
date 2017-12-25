# python3_sanshao90_blog
python3_sanshao90_blog

，归档时过滤不到月份是怎么一回事呢？

post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')filter中有月份month时QuerySet为空，post_list = Post.objects.filter(created_time__year=year).order_by('-created_time')这样时QuerySet有值不为空。

使用filter过滤时间，只认年份不认月份是怎么回事呢？
把setting.py里的USE_TZ 设置成False就行了
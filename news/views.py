from django.shortcuts import render, get_object_or_404
from .models import News

# 1. 新闻列表页面
def news_list(request):
    # 获取数据库里所有的新闻
    newsAll = News.objects.all()
    return render(request, 'news/news_list.html', {'newsList': newsAll})

# 2. 新闻详情页面
def news_detail(request, id):
    # 根据点击的 ID 找出对应的新闻
    news = get_object_or_404(News, id=id)
    
    # 小亮点：每次打开详情页，浏览量自动 +1
    news.views += 1
    news.save()
    
    return render(request, 'news/news_detail.html', {'news': news})
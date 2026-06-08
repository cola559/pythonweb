from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.core.paginator import Paginator

def news_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    
    if category_id:
        all_news = News.objects.filter(category_id=category_id)
    else:
        all_news = News.objects.all()

    # 分页功能：每页 4 篇
    paginator = Paginator(all_news, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 热门推荐（阅读量最高的前 3 篇）
    hot_news = News.objects.order_by('-views')[:3]

    return render(request, 'news/news_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'hot_news': hot_news,
        'current_category': category_id,
    })

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    # 增加阅读量统计
    news.views += 1
    news.save(update_fields=['views'])
    return render(request, 'news/news_detail.html', {'news': news})
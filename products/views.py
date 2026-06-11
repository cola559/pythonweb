from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product

# 1. 算力产品列表页（带动态分类、带大厂级分页器）
def product_list(request):
    # 接收前端传过来的品类筛选条件，比如：?type=认知大模型
    p_type = request.GET.get('type', 'all')
    
    if p_type == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(productType=p_type)
        
    # 核心：调用 Django 内置分页器，设定每页显示 3 个产品
    paginator = Paginator(products, 3)
    page = request.GET.get('page') # 获取当前是第几页
    
    try:
        productList = paginator.page(page)
    except PageNotAnInteger:
        # 如果 page 不是整数，默认展示第一页
        productList = paginator.page(1)
    except EmptyPage:
        # 如果页码超出了最大范围，展示最后一页
        productList = paginator.page(paginator.num_pages)
        
    return render(request, 'products/productList.html', {
        'productList': productList,
        'p_type': p_type,
    })

# 2. 算力详情页
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/productDetail.html', {'product': product})
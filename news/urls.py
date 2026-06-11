from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    # 访问 /news/ 时，展示新闻列表
    path('', views.news_list, name='news_list'),
    # 访问 /news/数字/ 时，展示对应的新闻详情
    path('<int:id>/', views.news_detail, name='news_detail'),
]
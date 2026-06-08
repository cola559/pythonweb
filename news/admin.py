from django.contrib import admin
from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish_date', 'views')
    list_filter = ('category',) # 分类筛选
    search_fields = ('title', 'summary') # 搜索功能
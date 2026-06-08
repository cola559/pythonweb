from django.db import models
from django.utils import timezone

# 新闻分类模型
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="分类名称")
    
    class Meta:
        verbose_name = "新闻分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 新闻模型
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="新闻标题")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    summary = models.TextField(verbose_name="新闻摘要")
    content = models.TextField(verbose_name="正文内容")
    publish_date = models.DateTimeField(default=timezone.now, verbose_name="发布时间")
    views = models.PositiveIntegerField(default=0, verbose_name="阅读量") # 用于热门推荐

    class Meta:
        verbose_name = "新闻动态"
        verbose_name_plural = verbose_name
        ordering = ['-publish_date'] # 默认按时间倒序排

    def __str__(self):
        return self.title
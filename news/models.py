from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    NEWS_CHOICES = (
        ('企业要闻', '企业要闻'),
        ('前沿科技', '前沿科技'), # 带有星云特色的分类
        ('通知公告', '通知公告'),
    )
    title = models.CharField(max_length=200, verbose_name="新闻标题")
    newType = models.CharField(choices=NEWS_CHOICES, max_length=50, verbose_name='新闻类型', default='前沿科技')
    
    # 核心：使用 CKEditor 替代普通文本，让你能像用 Word 一样排版
    content = RichTextUploadingField(verbose_name="正文内容")
    
    publishDate = models.DateTimeField(default=timezone.now, verbose_name="发布时间")
    views = models.PositiveIntegerField(default=0, verbose_name="阅读量")
    photo = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='新闻封面')

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "AI 资讯"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
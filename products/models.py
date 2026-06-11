from django.db import models
from django.utils import timezone

class Product(models.Model):
    PRODUCT_CHOICES = (
        ('认知大模型', '认知大模型陣列'),
        ('分布式算力', '分布式算力網絡'),
        ('隐私计算', '隐私计算与安全盾'),
    )
    title = models.CharField(max_length=100, verbose_name="产品名称")
    productType = models.CharField(choices=PRODUCT_CHOICES, max_length=50, verbose_name="算力品类", default='认知大模型')
    price = models.CharField(max_length=50, verbose_name="算力资费", default="按需计费 (Token)")
    description = models.TextField(verbose_name="功能核心描述")
    photo = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="算力展示长图")
    publishDate = models.DateTimeField(default=timezone.now, verbose_name="上线发布时间")

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "AI 算力矩阵"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
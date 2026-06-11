from django.db import models
from django.utils import timezone

class ContactTicket(models.Model):
    name = models.CharField(max_length=50, verbose_name="联系人/企业名称")
    phone = models.CharField(max_length=20, verbose_name="联系电话")
    email = models.EmailField(verbose_name="电子邮箱")
    requirement = models.TextField(verbose_name="算力需求/业务描述")
    
    # 核心：允许用户上传附件（比如需求文档、系统架构图等）
    document = models.FileField(upload_to='contact_docs/', blank=True, null=True, verbose_name="附件文档")
    
    submit_date = models.DateTimeField(default=timezone.now, verbose_name="提交时间")
    is_processed = models.BooleanField(default=False, verbose_name="是否已处理")

    class Meta:
        ordering = ['-submit_date']
        verbose_name = "接入咨询工单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name} 的接入申请"
from django.contrib import admin
from .models import ContactTicket

@admin.register(ContactTicket)
class ContactTicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'submit_date', 'is_processed')
    list_filter = ('is_processed', 'submit_date')
    search_fields = ('name', 'phone', 'requirement')
    # 在后台允许直接点击修改处理状态
    list_editable = ('is_processed',)
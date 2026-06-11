from django import forms
from .models import ContactTicket

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactTicket
        # 指定前端可以填写的字段（注意：我们不需要让用户填 submit_date 和 is_processed）
        fields = ['name', 'phone', 'email', 'requirement', 'document']
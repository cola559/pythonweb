from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        # 注意：处理文件上传必须加上 request.FILES
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # 直接保存到数据库
            # 发送成功弹窗提示语
            messages.success(request, '🚀 您的接入申请与相关文档已成功提交！星云架构师将在 24 小时内与您联系。')
            return redirect('contact:contact') # 提交后刷新页面，清空表单
        else:
            messages.error(request, '⚠️ 表单填写有误，请检查后重新提交。')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
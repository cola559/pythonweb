"""
URL configuration for hjl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('', include('pages.urls')), 
    path('news/', include('news.urls')),
    path('service/', include('serviceApp.urls')),
    path('products/', include('products.urls')), #  产品的路径
    
    # 👇 富文本编辑器上传图片的专属路由
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # 👇 全文搜索路由
    path('search/', include('haystack.urls')),
]

# 👇 极其重要：在开发环境下，允许浏览器直接访问我们上传到 media 文件夹里的图片
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views

app_name = 'serviceApp'

urlpatterns = [
    # 渲染服务支持主页面
    path('', views.platform_view, name='platform'),
    # 资料流式下载接口
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),
    # 在线人脸检测的 API 接口
    path('facedetectDemo/', views.facedetectDemo, name='facedetectDemo'),
]
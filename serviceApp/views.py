from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import escape_uri_path  # 解决中文名下载乱码报错
import os
import cv2
import base64
import numpy as np
from .models import Doc

# ================= 1. 资料页面渲染 =================
def platform_view(request):
    docList = Doc.objects.all()
    return render(request, 'serviceApp/platForm.html', {'docList': docList})

# ================= 2. 大文件流式下载 =================
def read_file(file_name, size):
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break

def getDoc(request, id):
    doc = get_object_or_404(Doc, id=id)
    filepath = doc.file.path
    filename = os.path.basename(filepath) 
    
    response = StreamingHttpResponse(read_file(filepath, 512))
    response['Content-Type'] = 'application/octet-stream'
    # 使用 escape_uri_path 完美支持中文文件名
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(filename))
    return response

# ================= 3. 人脸检测引擎 =================
face_detector_path = "serviceApp/haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(face_detector_path) 

def read_image(stream=None):
    if stream is not None:
        data_temp = stream.read()
        img = np.asarray(bytearray(data_temp), dtype="uint8")
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        return img

@csrf_exempt
def facedetectDemo(request):
    """供网页在线体验的 API 接口"""
    result = {}
    if request.method == "POST":
        if request.FILES.get('image') is not None:
            img = read_image(stream=request.FILES["image"])
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if img.shape[2] == 3 else img
            
            # 执行检测
            values = face_detector.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            
            for (w, x, y, z) in values:
                # 绘制星云赛博蓝框 (0, 242, 254)
                cv2.rectangle(img, (w, x), (w+y, x+z), (0, 242, 254), 2) 
            
            retval, buffer_img = cv2.imencode('.jpg', img)
            img64 = base64.b64encode(buffer_img)
            img64 = str(img64, encoding='utf-8')
            
            result["img64"] = img64
            return JsonResponse(result)
    return JsonResponse(result)
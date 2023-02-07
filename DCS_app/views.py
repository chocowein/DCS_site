from django.shortcuts import render, redirect
from django.http import HttpResponse

from DCS_app import models
import cv2
import numpy as np


def detail(request):
    return HttpResponse("detail page[no data]")


def sub_color(src, K):
    Z = src.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape((src.shape))

def mosaic(img, alpha):
    h, w, ch = img.shape
    img = cv2.resize(img,(int(w*alpha), int(h*alpha)))
    img = cv2.resize(img,(w, h), interpolation=cv2.INTER_NEAREST)
    return img

def pixel_art(img, alpha=2, K=4):
    img = mosaic(img, alpha)
    return sub_color(img, K)

def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        img = pixel_art(img)
        _, img_encoded = cv2.imencode('.jpg', img)
        return render(request, 'index.html', {'img_encoded': img_encoded.tobytes()})
    return render(request, 'DCS_app/index.html')

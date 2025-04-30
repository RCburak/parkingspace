from django.shortcuts import render
from django.http import StreamingHttpResponse
from .video_processing import get_video_capture_1, check_parking_space_1  # 1. video için
from .video_processing2 import get_video_capture_2, check_parking_space_2  # 2. video için
import cv2
import numpy as np

# İlk video
cap1 = get_video_capture_1()

def video_feed_1():
    while True:
        success, img = cap1.read()
        if not success:
            cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        check_parking_space_1(imgDilate, img)  # 1. video için park yeri kontrolü

        ret, jpeg = cv2.imencode('.jpg', img)
        if ret:
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def parking_video(request):
    return StreamingHttpResponse(video_feed_1(), content_type='multipart/x-mixed-replace; boundary=frame')

# İkinci video
cap2 = get_video_capture_2()

def video_feed_2():
    while True:
        success, img = cap2.read()
        if not success:
            cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        check_parking_space_2(imgDilate, img)  # 2. video için park yeri kontrolü

        ret, jpeg = cv2.imencode('.jpg', img)
        if ret:
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def parking_video_2(request):
    return StreamingHttpResponse(video_feed_2(), content_type='multipart/x-mixed-replace; boundary=frame')

# Anasayfa
def home(request):
    return render(request, 'home.html')

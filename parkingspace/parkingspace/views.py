from django.shortcuts import render
from django.http import StreamingHttpResponse
from park.models import ParkingLocation
from .video_processing import get_video_capture_1, check_parking_space_1  # 1. video için
from .video_processing2 import get_video_capture_2, check_parking_space_2  # 2. video için
import cv2
import numpy as np

# 1. video
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

        check_parking_space_1(imgDilate, img)

        ret, jpeg = cv2.imencode('.jpg', img)
        if ret:
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def parking_video(request):
    return StreamingHttpResponse(video_feed_1(), content_type='multipart/x-mixed-replace; boundary=frame')


# 2. video
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

        check_parking_space_2(imgDilate, img)

        ret, jpeg = cv2.imencode('.jpg', img)
        if ret:
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def parking_video_2(request):
    return StreamingHttpResponse(video_feed_2(), content_type='multipart/x-mixed-replace; boundary=frame')


def Ebebek(request):
    # Video akışlarını template'e direkt gönderiyoruz
    return render(request, 'Ebebek.html', {
        'video_feed_1': parking_video,  # 1. video akışı
        'video_feed_2': parking_video_2  # 2. video akışı
    })
def AkasyaAWM(request):
    # Video akışlarını template'e direkt gönderiyoruz
    return render(request, 'AkasyaAWM.html', {
        'video_feed_1': parking_video,  # 1. video akışı
        'video_feed_2': parking_video_2  # 2. video akışı
    })

# Ana sayfa - ParkingLocation'ları dinamik gönderiyoruz
def home(request):
    locations = ParkingLocation.objects.all()  # Veritabanındaki tüm ParkingLocationları alıyoruz
    return render(request, 'home.html', {'locations': locations})

import cv2
import numpy as np
import cvzone

# Video dosyasının yolu
video_path = r"media/carparkk.mp4"

# Video açma
cap = cv2.VideoCapture(video_path)

# 1. video için elle girilen park yeri koordinatları
posList_1 = [
    ((155, 250), (280, 450)),  # Park yeri 1
    ((340, 250), (450, 450)),  # Park yeri 2
    ((510, 250), (640, 450)),  # Park yeri 3
    ((705, 250), (830, 450)),  # Park yeri 4
    ((875, 250), (1000, 450)), # Park yeri 5
    ((1070, 250), (1150, 430)) # Park yeri 6
]

# 1. video için park yerlerini kontrol etme
def check_parking_space_1(imgPro, img):
    spaceCounter = 0
    for start, end in posList_1:
        x1, y1 = start
        x2, y2 = end
        x, y = min(x1, x2), min(y1, y2)
        w, h = abs(x2 - x1), abs(y2 - y1)

        # Koordinatları kesme ve park yerini kontrol etme
        imgCrop = imgPro[y:y + h, x:x + w]
        count = cv2.countNonZero(imgCrop)

        # Park yeri boşsa yeşil, doluysa kırmızı
        if count < 3150:
            color = (0, 255, 0)  # Yeşil renk
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)  # Kırmızı renk
            thickness = 2

        # Park yerinin etrafına dikdörtgen çizme
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)

    # Ekranda boş park yerlerinin sayısını gösterme
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList_1)}', 
                       (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

# Video kaynağını almak için fonksiyon
def get_video_capture_1():
    return cap  # 1. video kaynağını döndürüyoruz

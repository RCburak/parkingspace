import cv2
import pickle
import cvzone
import numpy as np

# CarParkPos dosyasındaki koordinatlar
with open('parkingspace/CarParkPos', 'rb') as f:
    posList_2 = pickle.load(f)

# Park yerlerinin boyutu
width, height = 107, 48

# 2. video için video kaynağı
def get_video_capture_2():
    return cv2.VideoCapture("media/carPark.mp4")  # 2. video kaynağını döndürüyoruz

# 2. video için park yerlerini kontrol etme
def check_parking_space_2(imgPro, img):
    spaceCounter = 0
    for pos in posList_2:
        x, y = pos
        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)
        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList_2)}', (100, 50),
                       scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

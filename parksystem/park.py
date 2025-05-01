import cv2
import pickle
import cvzone
import numpy as np

# Video feed
video_path = r"image\carPark.mp4"
cap = cv2.VideoCapture(video_path)

# Park yeri pozisyonlarının yüklendiği dosya
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

# Sıralama işlemi, burada 'posList' verisi yüklendikten sonra yapılmalı
posList = sorted(posList, key=lambda pos: (pos[1], pos[0]))

width, height = 107, 48  # Park yeri boyutları

def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)  # Beyaz (boş) alanın sayımı

        # Eğer boş yer varsa, yeşil renkte ve kalın çizgi çizeriz
        if count < 900:  # Boş yerin sayımı (threshold değerini değiştirebilirsiniz)
            color = (0, 255, 0)  # Yeşil renk
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)  # Kırmızı renk
            thickness = 2

        # Park yerlerini dikdörtgen ile işaretle
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

    # Boş park yerlerinin sayısını ekranda göster
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

while True:
    # Video'nun sonuna gelindiyse başa sar
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    success, img = cap.read()  # Görüntüyü al
    if not success:  # Video biterse döngüyü durdur
        break

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Gri tonlama
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)  # Bulanıklaştırma
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)  # Uyarlanabilir eşikleme
    imgMedian = cv2.medianBlur(imgThreshold, 5)  # Ortalamalı bulanıklaştırma
    kernel = np.ones((3, 3), np.uint8)  # Morfolojik işlem için çekirdek
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)  # Genişletme işlemi

    # Park yerlerini kontrol et
    checkParkingSpace(imgDilate)

    # Ekranda sonucu göster
    cv2.imshow("Image", img)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):  
        break
 
     
cap.release()
cv2.destroyAllWindows()
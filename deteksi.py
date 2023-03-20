import cv2
from matplotlib import pyplot as plt

# Baca gambar
img = cv2.imread('KEIHIN/deteksi/detect.jpg')

# Tentukan range warna merah pada HSV
lower_red = (130.0, 62.0, 0, 0)
upper_red = (255.0, 255.0, 255.0, 0)
lower_red2 = (170, 50, 50)
upper_red2 = (180, 255, 255)

# Konversi ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Masking untuk merah
mask1 = cv2.inRange(hsv, lower_red, upper_red)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2

# Cari kontur
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop untuk setiap kontur
for cnt in contours:
    # Hitung luas kontur
    area = cv2.contourArea(cnt)
    # Jika luas kontur lebih kecil dari 500, lewati kontur ini
    if area < 10:
        continue

    # Dapatkan koordinat kotak pembatas kontur
    (x, y, w, h) = cv2.boundingRect(cnt)

    # Gambar kotak pada gambar
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(img, "({}, {}, {}, {})".format(h/1000, w/1000, x/1000, y/1000), (x, y),
                cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 255))

    # Tampilkan koordinat kotak
    print("Kotak berwarna merah ditemukan pada koordinat (h, w, x, y) : ({}, {}, {}, {})".format(
        h/1000, w/1000, x/1000, y/1000))

# Save the image to a file
#cv2.imwrite('hasil.jpg', img)
plt.imshow(img)
plt.show()

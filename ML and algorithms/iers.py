import cv2
import numpy as np

# добавил нам пай т.к. без него вообще жесть
img = cv2.imread('girl.jpg')
size = img.shape
size_h = size[0]
size_w = size[1]

padd = int(input()) - 1  # взял не нечётный квадрат а дал -1
dtype=np.uint8
image = np.zeros((size_h + padd, size_w + padd, size[2]), dtype=np.uint8)  # создали нулевую матрицу которую будем заполнять не считая границы

for high in range(int(padd / 2), int(size_h + padd / 2)):
    for width in range(int(padd / 2), int(size_w + padd / 2)):
        image[high, width, :] = img[high-padd//2, width-padd//2, :]



for rgb in range(3):
    for high in range(int(padd / 2), int(size_h + padd / 2)):
        for width in range(int(padd / 2), int(size_w + padd / 2)):
            arr = []
            for ker_h in range(padd + 1):
                for ker_w in range(padd + 1):
                    arr.append(image[high + ker_h - padd // 2, width + ker_w - padd // 2, rgb])
            img[high-padd//2, width-padd//2, rgb] = sum(arr) / 9

cv2.imshow("собака", img)
cv2.waitKey(0)  # проверки


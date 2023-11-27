import cv2
import numpy as np
# добавил нам пай для вычисление

img = cv2.imread('girl.jpg')
img1 = img/255
size = img.shape
size_h = size[0]
size_w = size[1]

padd = int(input()) - 1  # взял не нечётный квадрат а дал -1
image = np.zeros((size_h + padd, size_w + padd, size[2]),
                 dtype=np.uint8)


for high in range(int(padd / 2), int(size_h + padd / 2)):  # цикл для копирования изображения в новое
    for width in range(int(padd / 2), int(size_w + padd / 2)):
        image[high, width, :] = img[high-padd//2, width-padd//2, :]

for rgb in range(3):  # цикл заполнения массива
    for high in range(int(padd / 2), int(size_h + padd / 2)):
        for width in range(int(padd / 2), int(size_w + padd / 2)):
            arr = []  # массив цветов со значениями пикселей
            for ker_h in range(padd + 1):
                for ker_w in range(padd + 1):
                    arr.append(image[high + ker_h - padd // 2, width + ker_w - padd // 2, rgb])  # добавление значения
            img[high-padd//2, width-padd//2, rgb] = int(sum(arr) / (padd+1)**2)
img = img/255
im_sharp = np.clip(2*img1 - img, 0, 1)
cv2.imshow("dogg", im_sharp)
cv2.waitKey(0)
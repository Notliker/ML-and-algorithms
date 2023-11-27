import random

import cv2
import numpy as np


img = cv2.imread('girl.jpg')  # открытие изображения
size = img.shape  # измерение изображения (высота*ширина*rgb)
size_h = size[0]
size_w = size[1]

padd = int(input("Введите нечётную сторону квадрата фильтра, >1 \n")) - 1  # взял четное число
if (padd <= 1) or ((padd % 2) != 0):
    print("неверное число")
    exit(1)

image = np.zeros((size_h + padd, size_w + padd, size[2]), dtype=np.uint8)  # создали нулевую матрицу с границами

for high in range(int(padd / 2), int(size_h + padd / 2)):  # цикл для копирования изображения в новое
    for width in range(int(padd / 2), int(size_w + padd / 2)):
        if random.random() >= 0.85:
            image[high, width, :] = 255
        elif random.random() <= 0.15:
            image[high, width, :] = 0
        else:
            image[high, width, :] = img[high-padd//2, width-padd//2, :]

cv2.imshow("final", image)  # вывод картинки
cv2.waitKey(0)  # картинка не исчезает

for rgb in range(3):  # цикл заполнения массива
    for high in range(int(padd / 2), int(size_h + padd / 2)):
        for width in range(int(padd / 2), int(size_w + padd / 2)):
            arr = []  # массив цветов со значениями пикселей
            for ker_h in range(padd + 1):
                for ker_w in range(padd + 1):
                    arr.append(image[high + ker_h - padd // 2, width + ker_w - padd // 2, rgb])  # добавление значения
            img[high-padd//2, width-padd//2, rgb] = np.median(arr)  # формула для blur


cv2.imshow("final", img)  # вывод картинки
cv2.waitKey(0)  # картинка не исчезает
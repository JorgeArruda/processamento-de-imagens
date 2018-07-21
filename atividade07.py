#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from atividade06 import segmentar_iterativo
from atividade01 import image_not


coin_c = cv2.imread('Imagens/coins.jpg', cv2.IMREAD_GRAYSCALE)
coin = cv2.imread('Imagens/coins.jpg')
foto_01 = cv2.imread('Imagens/foto01.png', cv2.IMREAD_GRAYSCALE)
foto_02 = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)
text_01 = cv2.imread('Imagens/text1.png', cv2.IMREAD_GRAYSCALE)
text_02 = cv2.imread('Imagens/text2.png', cv2.IMREAD_GRAYSCALE)
text_03 = cv2.imread('Imagens/text3.jpg', cv2.IMREAD_GRAYSCALE)
bio_01 = cv2.imread('Imagens/ima01.png', cv2.IMREAD_GRAYSCALE)
bio_02 = cv2.imread('Imagens/bio01.png', cv2.IMREAD_GRAYSCALE)
bio_03 = cv2.imread('Imagens/bio02.png', cv2.IMREAD_GRAYSCALE)
bird = cv2.imread('Imagens/bird.png')
bird_c = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite = cv2.imread('Imagens/dragonite.png')
dragonite_gray = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)
rosa = cv2.imread('Imagens/rosa.png')
rosa_gray = cv2.imread('Imagens/rosa.png', cv2.IMREAD_GRAYSCALE)
girl = cv2.imread('Imagens/foto02.png')
girl_gray = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)


def watershed(image, image_color):
    gradiente = segmentar_iterativo(image)
    gradiente_inverso = image_not(gradiente)

    kernel = np.ones((3, 3), np.uint8)
    thresh = gradiente_inverso
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)

    gradiente_erode = cv2.erode(opening, kernel, iterations=13)

    gradiente_erode = np.uint8(gradiente_erode)
    unknown = cv2.subtract(gradiente_inverso, gradiente_erode)

    ret, markers = cv2.connectedComponents(gradiente_erode)

    markers = markers+1
    markers[unknown == 255] = 0

    markers = cv2.watershed(image_color, markers)
    image_color[markers == -1] = [255, 255, 0]
    return image_color


if __name__ == '__main__':
    image_gray = dragonite_gray
    image = dragonite
    cv2.imshow('Imagem 01', image)
    cv2.imshow('Resultado - Watershed', watershed(image_gray, image))
    cv2.waitKey(0)
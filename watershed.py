#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from atividade06 import segmentar_iterativo
from atividade01 import image_not

coin_c = cv2.imread('Imagens/coins.jpg', cv2.IMREAD_GRAYSCALE)
coin = cv2.imread('Imagens/coins.jpg')

def watershed(image, image_color):
    print('watershed', image.shape)
    cv2.imshow('Image', image)
    gradiente = segmentar_iterativo(image)
    cv2.imshow('Gradiente', gradiente)
    gradiente_inverso = image_not(gradiente)
    cv2.imshow('Gradiente inverso', gradiente_inverso)

    kernel = np.ones((3,3),np.uint8)
    thresh = gradiente_inverso
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 3)

    gradiente_erode = cv2.erode(opening, kernel, iterations = 13)
    cv2.imshow('Gradiente erode', gradiente_erode)

    gradiente_erode = np.uint8(gradiente_erode)
    unknown = cv2.subtract(gradiente_inverso,gradiente_erode)
    cv2.imshow('gradiente_inverso - gradiente_erode', unknown)

    ret, markers = cv2.connectedComponents(gradiente_erode)
    
    markers = markers+1
    markers[unknown==255] = 0
    cv2.imshow('markers', markers)

    markers = cv2.watershed(image_color, markers)
    image_color[markers == -1] = [255,255,0]
    cv2.imshow('Resultado - Watershed', image_color)

    cv2.waitKey(0)


if __name__=='__main__':
    image = coin_c
    watershed(image, coin)
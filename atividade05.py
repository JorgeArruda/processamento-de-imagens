#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from cv2 import cv2
import math

foto_01 = cv2.imread('Imagens/foto01.png', cv2.IMREAD_GRAYSCALE)
foto_02 = cv2.imread('Imagens/foto02.png')
bio_01 = cv2.imread('Imagens/bio01.png')
bio_02 = cv2.imread('Imagens/bio02.png')
bird = cv2.imread('Imagens/bird.png')
dragonite = cv2.imread('Imagens/dragonite.png')
rosa = cv2.imread('Imagens/rosa.png')
rosa_gray = cv2.imread('Imagens/rosa.png', cv2.IMREAD_GRAYSCALE)
girl = cv2.imread('Imagens/foto02.png')
girl_gray = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)

def dithering_basico(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    # image = addZero(image)
    # print("\n Imagem(addZeros) ", image.shape)
    
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0],image.shape[1]), numpy.uint8)
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                result[linha,coluna] = 0 if image[linha,coluna] <= 127 else 255
    else:
        result = numpy.zeros((image.shape[0],image.shape[1],image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                for canal in range(0,image.shape[2]):
                    result[linha,coluna,canal] = 0 if image[linha,coluna,canal] <= 127 else 255
    return result

if (__name__=='__main__'):
    image = girl
    cv2.imshow('Image', image)
    cv2.imshow('Dithering basico', dithering_basico(image))
    image = girl_gray
    cv2.imshow('Image grayscale', image)
    cv2.imshow('Dithering basico - grayscale', dithering_basico(image))
    cv2.waitKey(0)
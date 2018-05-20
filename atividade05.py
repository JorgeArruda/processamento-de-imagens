#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from cv2 import cv2
import random
# Dithering:
#     - Básico
#     - Aleatório
#     - Periódico
#     - Aperiódico(Floyd-Steimberg)

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

def dithering_basico(image, lessgreater=[0, 255], limiar=127):
    print("Image dimensions ",image.shape)
    
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0],image.shape[1]), numpy.uint8)
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                result[linha,coluna] = lessgreater[0] if image[linha,coluna] <= limiar else lessgreater[1]
    else:
        result = numpy.zeros((image.shape[0],image.shape[1],image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                for canal in range(0,image.shape[2]):
                    result[linha,coluna,canal] = lessgreater[0] if image[linha,coluna,canal] <= limiar else lessgreater[1]
    return result

def dithering_random(image, rangee=(-100,0)):
    print("Image dimensions ",image.shape)
    
    if len(image.shape) == 2:
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                result[linha,coluna] = 0 if (image[linha,coluna]+random.randrange(rangee[0], rangee[1])) <= 127 else 255
    else:
        result = numpy.zeros((image.shape[0],image.shape[1],image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                for canal in range(0,image.shape[2]):
                    result[linha,coluna,canal] = 0 if (image[linha,coluna,canal]+random.randrange(rangee[0], rangee[1])) <= 127 else 255
    return result

def dithering_periodico(image):
    print("Image dimensions ",image.shape)

    if len(image.shape) == 2:
        result = numpy.array(image)
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                i = linha % 3
                j = coluna % 3
                if (image[linha,coluna] > image[i, j]):
                    result[linha,coluna] = 0
                else:
                    result[linha,coluna] = 255
    else:
        result = numpy.zeros((image.shape[0],image.shape[1],image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                for canal in range(0,image.shape[2]):
                    i = linha % 3
                    j = coluna % 3
                    if (image[linha,coluna, canal] > image[i, j, canal]):
                        result[linha,coluna, canal] = 0
                    else:
                        result[linha,coluna] = 255
    return result

def dithering_aperiodico(image):
    print("Image dimensions ",image.shape)
    black = 0
    white = 255
    threshold = (black+white)/2
    if len(image.shape) == 2:
        result = numpy.array(image)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                # if (image[linha, coluna] < threshold):
                #     error = image[linha, coluna] - black
                #     image[linha, coluna] = black
                # else:
                #     error = image[linha, coluna] - white
                #     image[linha, coluna] = white
                # image[linha+1, coluna] += round((3/8)*error)
                # image[linha, coluna-1] += round((3/8)*error)
                # image[linha+1, coluna-1] += round(error/4)
                if (image[linha, coluna] < threshold):
                    error = black - image[linha, coluna]
                    image[linha, coluna] = black
                else:
                    error = white - image[linha, coluna]
                    image[linha, coluna] = white
                image[linha+1, coluna] += round((7/16)*error)
                image[linha, coluna+1] += round((5/16)*error)
                image[linha+1, coluna+1] += round((1/16)*error)
                image[linha, coluna+1] += round((3/16)*error)

    return result


if (__name__=='__main__c'):
    image = girl
    cv2.imshow('Image', image)
    cv2.imshow('Dithering basico', dithering_basico(image))
    image = girl_gray
    cv2.imshow('Image grayscale', image)
    cv2.imshow('Dithering basico - grayscale', dithering_basico(image))
    cv2.waitKey(0)
if (__name__=='__main__'):
    image = rosa
    cv2.imshow('Image', image)
    # 
    image = girl_gray
    cv2.imshow('Image grayscale', image)
    cv2.imshow('Dithering aperiodico - grayscale', dithering_aperiodico(image))
    cv2.waitKey(0)

    for item in range(3, 0, -1):
        a = (1+1+1+1+1/
            +1+1+1)
        print(a)
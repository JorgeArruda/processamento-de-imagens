#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from cv2 import cv2

from atividade05 import dithering_basico

foto_01 = cv2.imread('Imagens/foto01.png', cv2.IMREAD_GRAYSCALE)
foto_02 = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)
bio_01 = cv2.imread('Imagens/bio01.png', cv2.IMREAD_GRAYSCALE)
bio_02 = cv2.imread('Imagens/bio02.png', cv2.IMREAD_GRAYSCALE)
bird = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)
rosa = cv2.imread('Imagens/rosa.png')
rosa_gray = cv2.imread('Imagens/rosa.png', cv2.IMREAD_GRAYSCALE)
girl = cv2.imread('Imagens/foto02.png')
girl_gray = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)


def segmentar(image, limiar):
    # image_less = numpy.array(image)
    # image_greater = numpy.array(image)
    pixels_less = []
    pixels_greater = []
    if len(image.shape) == 2:
        for linha in range(1,image.shape[0]):
            for coluna in range(1,image.shape[1]):
                if image[linha,coluna] <= limiar:
                    pixels_less.append(image[linha,coluna])
                else:
                    pixels_greater.append(image[linha,coluna])
    # else:
    #     for linha in range(1,image.shape[0]):
    #         for coluna in range(1,image.shape[1]):
    #             for canal in range(0,image.shape[2]):
    #                 if image[linha, coluna, canal] <= limiar:
    #                     pixels_less.append(image[linha, coluna ,canal])
    #                 else:
    #                     pixels_greater.append(image[linha, coluna, canal])    return result

    return (pixels_less, pixels_greater)

def media(elements):
    if type(elements) != list:
        return 'Argument invalid'
    result = 0
    for item in elements:
        result += item
    return result/len(elements)

def segmentar_iterativo(image, variacao=0.1):
    limiar = numpy.average(image)
    print('\tLimiar:', limiar,'\n')
    while (True):
        (pixels_less, pixels_greater) = segmentar(image, limiar)
        med = ( media(pixels_less) , media(pixels_greater) )
        print('Media pixels_less: ', med[0])
        print('Media pixels_greater: ', med[1])
        if abs(limiar - ( med[0]+med[1] )/2) <= 10:
            break
        limiar = ( med[0] + med[1] ) / 2
        print('\tLimiar:', limiar,'\n')
    print('\tLimiar:', limiar,'\n')

    return dithering_basico(image, limiar)

    
if __name__=='__main__':
    image = foto_01
    cv2.imshow('Image 01', image)
    image_seg = segmentar_iterativo(image)
    cv2.imshow('Limiarizacao iterativa 01', image_seg)
    image = bird
    cv2.imshow('Image 02', image)
    image_seg = segmentar_iterativo(image)
    cv2.imshow('Limiarizacao iterativa 02', image_seg)
    image = foto_02
    cv2.imshow('Image 03', image)
    image_seg = segmentar_iterativo(image)
    cv2.imshow('Limiarizacao iterativa 03', image_seg)
    cv2.waitKey(0)    
    
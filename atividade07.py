#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from cv2 import cv2

from atividade02 import print_array, calc_histogama, image_histograma
from atividade03 import filtro_mediana, filtro_gaussiano, filtro_passaalta, filtro_convolucao
from atividade05 import dithering_basico, dithering_random

foto_01 = cv2.imread('Imagens/foto01.png', cv2.IMREAD_GRAYSCALE)
foto_02 = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)
text_01 = cv2.imread('Imagens/text1.png', cv2.IMREAD_GRAYSCALE)
text_02 = cv2.imread('Imagens/text2.png', cv2.IMREAD_GRAYSCALE)
text_03 = cv2.imread('Imagens/text3.jpg', cv2.IMREAD_GRAYSCALE)
bio_01 = cv2.imread('Imagens/ima01.png', cv2.IMREAD_GRAYSCALE)
bio_02 = cv2.imread('Imagens/bio01.png', cv2.IMREAD_GRAYSCALE)
bio_03 = cv2.imread('Imagens/bio02.png', cv2.IMREAD_GRAYSCALE)
bird = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)
rosa = cv2.imread('Imagens/rosa.png')
rosa_gray = cv2.imread('Imagens/rosa.png', cv2.IMREAD_GRAYSCALE)
girl = cv2.imread('Imagens/foto02.png')
girl_gray = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)

def calc_min(histograma):
    minimo_pos = []
    minimo_lista = []
    total_minimo = 0
    for x in range(1,len(histograma)-1):
        if ( histograma[x-1] > histograma[x] and histograma[x] < histograma[x+1] ):
            minimo_pos.append( (x, histograma[x]) )
            minimo_lista.append( x )
            total_minimo += histograma[x]
    minimo_pos.append(minimo_lista)
    minimo_pos.append(total_minimo)
    return minimo_pos

def calc_pos_min(image, minimo):
    pos_minimo = []
    if len(image.shape) != 2:
        return
    for linha in range(1,image.shape[0]):
        for coluna in range(1,image.shape[1]):
            if image[linha, coluna] in minimo:
                image[linha, coluna] = 0
                pos_minimo.append( [linha, coluna] )
    cv2.imshow('Image 1', image)
    return pos_minimo

if __name__=='__main__':
    image = foto_01
    cv2.imshow('Image', image)
    histograma = calc_histogama(image)
    print_array(histograma)
    minimo = calc_min(histograma)
    print('image original', minimo)
    calc_pos_min(image, minimo[-2])


    # image = filtro_gaussiano(image)
    # # image = filtro_convolucao(image)
    # # image = filtro_passaalta(image)
    # cv2.imshow('Image suavizada', filtro_mediana(image))
    # histograma = calc_histogama(image)
    # print_array(histograma)
    # print('image suavizada', calc_min(histograma))
    cv2.waitKey(0)
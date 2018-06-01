#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2

from atividade02 import print_array, calc_histogama, image_histograma
from atividade03 import filtro_mediana, filtro_gaussiano, filtro_passaalta, filtro_convolucao
from atividade05 import dithering_basico, dithering_random
from atividade06 import segmentar_iterativo

coin = cv2.imread('Imagens/coins.jpg', cv2.IMREAD_GRAYSCALE)
coin_c = cv2.imread('Imagens/coins.jpg')
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
    for linha in range(1,image.shape[0]-1):
        for coluna in range(1,image.shape[1]-1):
            if image[linha, coluna] in minimo:
                image[linha, coluna] = 0
                pos_minimo.append( [linha, coluna] )
            else:
                image[linha, coluna] = 255
    cv2.imshow('Image 1', image)
    return image, pos_minimo

if __name__=='__main__oi':
    image = coin
    image = filtro_gaussiano(image)
    # image = filtro_convolucao(image)
    # image = filtro_passaalta(image)d
    valor_min = np.amin(image)
    valor_max = np.amax(image)
    cv2.imshow('Image', image)
    image_seg = segmentar_iterativo(image, [255, 0])
    print (valor_max, valor_min)

    cv2.imshow('Image Binaria', image_seg)
    histograma = calc_histogama(image)
    print_array(histograma)
    minimo = calc_min(histograma)
    print('image original', minimo)
    template, pos_minimo = calc_pos_min(image, minimo[-2])
    cv2.imshow('Image template', template)
    # print('pos_minimo', pos_minimo)
    permamente = []
    bn=0
    while len(pos_minimo)!=0 and bn < 2 :
        p = pos_minimo.pop()
        permamente.append(p)
        vizinho = [[-1,-1], [-1,0], [-1,1],  [0, -1], [0,1],  [1,-1], [1,0], [1,1] ]
        for i in vizinho:
            q = [ p[0]+i[0], p[1]+i[1] ]
            if not( q in permamente ):
                template[ q[0], q[1] ] = template[ p[0], p[1] ]
                pos_minimo = q + pos_minimo
                template[ p[0], p[1] ] = 255
            else:
                if template[ q[0], q[1] ] == 0 and 0 == template[ p[0], p[1] ]:
                    template[ q[0], q[1] ] = 0
                else:
                    template[ p[0], p[1] ] = 255
            # template[ p[0], p[1] ] = 255
        bn += 1
    cv2.imshow('Image template 2', template)
            
            
    # p[0] = p[0] if p[0]==template.shape[0] else p[0]-1
    # p[1] = p[1] if p[1]==template.shape[1] else p[1]-1
    # q[0] = q[0] if q[0]==template.shape[0] else q[0]-1
    # q[1] = q[1] if q[1]==template.shape[1] else q[1]-1

    # image = filtro_gaussiano(image)
    # # image = filtro_convolucao(image)
    # # image = filtro_passaalta(image)
    # cv2.imshow('Image suavizada', filtro_mediana(image))
    # histograma = calc_histogama(image)
    # print_array(histograma)
    # print('image suavizada', calc_min(histograma))
    cv2.waitKey(0)

if __name__=='__main__':
    img = coin_c
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('Image1', thresh)

    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    cv2.imshow('Image2 - sure_bg', sure_bg)
    # cv2.imshow('Image2 - opening', opening)

    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    cv2.imshow('Image3 - sure_fg', sure_fg)
    cv2.imshow('Image3 - dist_transform', dist_transform)

    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)
    cv2.imshow('Image4', unknown)

    ret, markers = cv2.connectedComponents(sure_fg)
    
    markers = markers+1

    markers[unknown==255] = 0
    cv2.imshow('Image5', markers)

    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]
    cv2.imshow('Image6', img)
    cv2.waitKey(0)
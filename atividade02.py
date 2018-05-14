#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Atividade 02 Histograma
import numpy
from cv2 import cv2
import matplotlib.pyplot as plt
#import pandas

bird = cv2.imread('Imagens/bird.png')
dragonite = cv2.imread('Imagens/dragonite.png')
bird_01 = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite_01 = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)

print('Bird   [Linhas, Colunas, Canais]: ', bird.shape)
print('Dragonite [Linhas, Colunas, Canais]: ', dragonite.shape)

ima01 = cv2.imread('Imagens/ima01.png')
ima02 = cv2.imread('Imagens/ima01.png', cv2.IMREAD_GRAYSCALE)

print('ima01: ',ima01.shape)
print('ima02: ',ima02.shape)


def print_array(lista):
    y_axis = lista
    x_axis = range(len(y_axis))
    width_n = 0.8
    bar_color = 'black'

    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

def calc_histogam(image):
    histograma = [0] * 256
    # Calcular o histograma, contabilizando a quantidade de pixels para cada valor de cor
    for linha in range(image.shape[0]):
        for coluna in range(image.shape[1]):
            histograma[image[linha, coluna]] = histograma[image[linha, coluna]] + 1
    return histograma

def calc_histograma_acumulado(histograma):
    # Calcular o histograma acumulador
    for x in range(1,256):
        histograma[x] = histograma[x-1] + histograma[x]
    return histograma

def calc_histograma_equalizado(histograma, faixa = (0, 255)):
    # Calcular a equalização do histograma acumulador
    for x in range(1, len(histograma)):
        #print ' histograma[x] ', histograma[x], ' image.shape[0]*image.shape[1] ', image.shape[0]*image.shape[1], ' div ', float(float(histograma[x]) / float(image.shape[0]*image.shape[1]))
        histograma[x] = int(round((faixa[1]-faixa[0]) *( float(histograma[x]) / float(histograma[-1]) ) ))

    return histograma

def image_histograma(image):
    image = numpy.array(image)
    print('Imagem[',image.shape[0],'], qt. de pixels ',image.shape[0]*image.shape[1],':\n',image)

    histograma = calc_histogam(image)
    # print('\nHistograma:\n',histograma)
    print_array(histograma)

    histograma = calc_histograma_acumulado(histograma)
    print('\nHistograma greater value:\n',histograma[-1])
    print_array(histograma)

    histograma = calc_histograma_equalizado(histograma)
    # print('\nHistograma acumulado equalizado:\n',histograma)
    print_array(histograma)

    # Refatorar a imagem, utilizando os valores do histograma equalizado
    for linha in range(image.shape[0]):
        for coluna in range(image.shape[1]):
            image[linha, coluna] = histograma[image[linha, coluna]]
            #histograma[image[linha, coluna]] = histograma[image[linha, coluna]] + 1
    
    return image

cv2.imshow('Image ',image_histograma(ima02))
cv2.waitKey(0)
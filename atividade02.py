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

def image_histograma(image01):
    histograma = []
    histograma = [0] * 256
    image = numpy.array(image01)
    print('Histograma(',len(histograma),') vazio:\n',histograma)
    print('Imagem[',image01.shape[0],'], qt. de pixels ',image01.shape[0]*image01.shape[1],':\n',image01)
    cv2.imshow('Image01 - Antes', image01)

    # Calcular o histograma, contabilizando a quantidade de pixels para cada valor de cor
    for linha in range(image01.shape[0]):
        for coluna in range(image01.shape[1]):
            histograma[image01[linha, coluna]] = histograma[image01[linha, coluna]] + 1

    print('\nHistograma:\n',histograma)
    print_array(histograma)

    # Calcular o histograma acumulador
    for x in range(1,256):
        histograma[x] = histograma[x-1] + histograma[x]
    
    print('\nHistograma acumulado:\n',histograma)
    print_array(histograma)

    # Calcular a equalização do histograma acumulador
    for x in range(1,256):
        #print ' histograma[x] ', histograma[x], ' image01.shape[0]*image01.shape[1] ', image01.shape[0]*image01.shape[1], ' div ', float(float(histograma[x]) / float(image01.shape[0]*image01.shape[1]))
        histograma[x] = int(round(255 *( float(histograma[x]) / float(image01.shape[0]*image01.shape[1]) ) ))

    print('\nHistograma acumulado equalizado:\n',histograma)
    #print_array(histograma)

    # Refatorar a imagem, utilizando os valores do histograma equalizado
    for linha in range(image01.shape[0]):
        for coluna in range(image01.shape[1]):
            image01[linha, coluna] = histograma[image01[linha, coluna]]
            #histograma[image01[linha, coluna]] = histograma[image01[linha, coluna]] + 1
    cv2.imshow('Image01 - Equalizada', image01)
    cv2.waitKey(0)

image_histograma(ima02)
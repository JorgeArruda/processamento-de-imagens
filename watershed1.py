#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from atividade06 import segmentar_iterativo
from atividade01 import image_not

coin_c = cv2.imread('Imagens/coins.jpg', cv2.IMREAD_GRAYSCALE)
coin = cv2.imread('Imagens/coins.jpg')


def calc_pos_mark(markers):
    posicao = []
    for linha in range(1, markers.shape[0]-1):
        for coluna in range(1, markers.shape[1]-1):
            if markers[linha, coluna] == 250:
                posicao.append([linha, coluna])
    return posicao


def watershedd(image, markers):
    pontos = calc_pos_mark(markers)
    nivel_cinza = image[pontos[0][0], pontos[0][1]]
    fila = [0]*255
    fila[nivel_cinza] = pontos
    # print(fila)
    # return markers
    i = nivel_cinza
    visitados = []
    num_loop = 0
    while len(fila[i]) != 0:
        ponto = fila[i].pop()
        if (type(ponto) != list):  # and (ponto[0] == 0 or ponto[0] == markers.shape[0]-1 or ponto[1] == 0 or ponto[1] == markers.shape[1]-1):
            pass
        if type(ponto) == list:
            visitados.append(ponto)
            vizinho = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            for i in vizinho:
                # print(' i ', type(i), ' ponto ', type(ponto))
                q = [ponto[0]+i[0], ponto[1]+i[1]]
                nivel_cinza = image[q[0], q[1]]
                if not(q in visitados):
                    if fila[nivel_cinza] != 0:
                        fila[nivel_cinza].append(q)
                    else:
                        fila[nivel_cinza] = [q]

        num_loop += 1
    cv2.imshow('New image', image)
    return markers


def watershed(image, image_color):
    print('watershed', image.shape)
    cv2.imshow('Image', image)
    gradiente = segmentar_iterativo(image)
    cv2.imshow('Gradiente', gradiente)
    gradiente_inverso = image_not(gradiente)
    cv2.imshow('Gradiente inverso', gradiente_inverso)

    kernel = np.ones((3, 3), np.uint8)
    thresh = gradiente_inverso
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)

    gradiente_erode = cv2.erode(opening, kernel, iterations=13)
    cv2.imshow('Gradiente erode', gradiente_erode)

    gradiente_erode = np.uint8(gradiente_erode)
    unknown = cv2.subtract(gradiente_inverso, gradiente_erode)
    cv2.imshow('gradiente_inverso - gradiente_erode', unknown)

    ret, markers = cv2.connectedComponents(gradiente_erode)
    # gradiente_inverso é a imagem dos limites da barragem
    markers = markers+1
    markers[unknown == 255] = 0
    # markers[markers >= 1] = 250
    cv2.imshow('markers', markers)

    markers = cv2.watershed(image_color, markers)
    image_color[markers == -1] = [255, 255, 0]
    cv2.imshow('Resultado - Watershed', image_color)

    cv2.waitKey(0)


if __name__ == '__main__':
    image = coin_c
    watershed(image, coin)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from atividade06 import segmentar_iterativo
from atividade01 import image_not

coin_c = cv2.imread('Imagens/coins.jpg', cv2.IMREAD_GRAYSCALE)
coin = cv2.imread('Imagens/coins.jpg')


def addZero(matrix):
    
    if len(matrix.shape) == 2:
        # Inserir zeros no inicio de todas as linhas do array
        matrix = np.insert(matrix, 0, 0, axis=1)
        # Inserir zeros no final de todas as linhas do array
        matrix = np.insert(matrix, matrix.shape[1], 0, axis=1)

        # Criar uma linha de zeros
        linha01 = np.zeros((matrix.shape[1]), np.uint8)
        # Inserir a linha de zeros no inicio
        matrix = np.insert(matrix, 0, linha01, axis=0)
        # Inserir a linha de zeros no final
        matrix = np.insert(matrix, matrix.shape[0], linha01, axis=0)

    if len(matrix.shape) == 3:
        # Criar uma array de zeros, para um pixel
        pixel = np.zeros((matrix.shape[2]), np.uint8)
        # Inserir zeros no inicio de todas as linhas do array
        matrix = np.insert(matrix, 0, pixel, axis=1)
        # Inserir zeros no final de todas as linhas do array
        matrix = np.insert(matrix, matrix.shape[1], pixel, axis=1)

        # Criar uma linha de zeros
        linha = np.zeros((1, matrix.shape[1], 3), np.uint8)
        # Inserir a linha de zeros no inicio
        matrix = np.insert(matrix, 0, linha, axis=0)
        # Inserir a linha de zeros no final
        matrix = np.insert(matrix, matrix.shape[0], linha, axis=0)

    return matrix


def find(array, valor):
    """Retorna uma lista com os indices de todas as ocorrências de valor.\
    Realiza a pesquisa em um array numpy[x, y]"""
    temp = np.where(array == valor)
    linha = temp[0].tolist()
    coluna = temp[1].tolist()
    indices = np.array([linha, coluna], int)
    return indices.reshape(indices.shape[1], 2).tolist()


def listmin(array):
    """Retorna uma lista coms os valores que aparecem em array em ordem \
    crescente"""
    #  a.tolist()
    # array([[0., 2., 0., 0., 0., 0., 0., 0., 0., 6.]])
    # array.flatten()   # sorted(array)   # array.reshape(2,2)
    # np.unique(array)  # array.sort()
    listgray = sorted(np.unique(array))
    return listgray


def verifica(matriz):
    for i in range(len(matriz)):
        if len(matriz[i]) > 0:
            return i+1
    return False


def watershed(image, qt_min=10):
    # image = addZero(image)
    water = []
    listgray = listmin(image)
    fila = [[]]*255
    barragen = []
    print('Inicio, criação da fila de mínimos com as coordenados dos pixels\n')
    for nivel in range(0, qt_min, 1):
        fila[listgray[nivel]] = find(image, listgray[nivel])
        print(listgray[nivel], "   >>>   ", fila[listgray[nivel]])

    limit = 0
    gray = listgray[0]
    print("\nGray ", gray)
    while verifica(fila):
        # Retira o primeiro elemento da fila
        # print("fila[gray]  >", fila[gray])
        pixel = fila[gray].pop(0)
        # break
        water.append(pixel)
        vizinhos = [[-1, -1], [1, 1], [-1, 0], [0, -1], [1, 0], [0, 1], [-1, 1], [1, -1]]
        for v in vizinhos:
            vizinho = [pixel[0]+v[0], pixel[1]+v[1]]
            if not((vizinho[0] >= 0) and (vizinho[0] < image.shape[0]) and vizinho[1] >= 0 and vizinho[1] < image.shape[1]):
                break
            nivel_cinza = image[vizinho[0], vizinho[1]]

            if not(vizinho in water):
                fila[nivel_cinza].append(vizinho)
            else:
                water.remove(vizinho)
                barragen.append(vizinho)
        # print('iiiii', barragen)
        if (len(barragen) >= 30000):
            break
        if len(fila[gray]) == 0:
            limit += 1
            gray = listgray[limit]
            if gray >= len(fila):
                gray = 0
                print('gray')
        # if len(fila[gray]) == 0:
        #     gray += 1
        #     while len(fila[gray]) == 0:
        #         print('Alloo')
        #         gray += 1
        #         if gray > (len(fila)-1):
        #             # gray = 0
        #             limit += 4
        #         if limit >= 2:
        #             break
        # if limit >= 2:
        #     break
    print('Barragem', barragen)
    while len(barragen) != 0:
        (x, y) = barragen.pop()
        image[x, y] = 0
    return image

def watershedd(image, markers):
    pontos = markers  # calc_pos_mark(markers)
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


if __name__ == '__main__':
    image = coin_c
    cv2.imshow('coin_c', coin_c)
    haha = watershed(image)
    cv2.imshow('Barragem', haha)
    cv2.waitKey(0)
    # watershedd(image, coin)

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from cv2 import cv2
import math
from atividade01 import image_add_01, image_add, image_mult
from atividade03 import filtro_gaussiano
# Atividade 04 Realce de bordas:
#     - Sobel
#     - Prewitt
#     - Roberts
#     - Isotrópico

foto_01 = cv2.imread('Imagens/foto01.png', cv2.IMREAD_GRAYSCALE)
foto_02 = cv2.imread('Imagens/foto02.png')
bio_01 = cv2.imread('Imagens/bio01.png')
bio_02 = cv2.imread('Imagens/bio02.png')
bird = cv2.imread('Imagens/bird.png')
dragonite = cv2.imread('Imagens/dragonite.png')
bird_c = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite_c = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)
rosa = cv2.imread('Imagens/rosa.png')
girl = cv2.imread('Imagens/girl1.png')
rosa_c = cv2.imread('Imagens/rosa.png', cv2.IMREAD_GRAYSCALE)
girl_c = cv2.imread('Imagens/girl1.png', cv2.IMREAD_GRAYSCALE)
coin = cv2.imread('Imagens/coins.jpg')
coin_c = cv2.imread('Imagens/coins.jpg', cv2.IMREAD_GRAYSCALE)


def addZero(matrix):

    if len(matrix.shape) == 2:
        # Inserir zeros no inicio de todas as linhas do array
        matrix = numpy.insert(matrix, 0, 0, axis=1)
        # Inserir zeros no final de todas as linhas do array
        matrix = numpy.insert(matrix, matrix.shape[1], 0, axis=1)

        # Criar uma linha de zeros
        linha01 = numpy.zeros((matrix.shape[1]), numpy.uint8)
        # Inserir a linha de zeros no inicio
        matrix = numpy.insert(matrix, 0, linha01, axis=0)
        # Inserir a linha de zeros no final
        matrix = numpy.insert(matrix, matrix.shape[0], linha01, axis=0)

    if len(matrix.shape) == 3:
        # Criar uma array de zeros, para um pixel
        pixel = numpy.zeros((matrix.shape[2]), numpy.uint8)
        # Inserir zeros no inicio de todas as linhas do array
        matrix = numpy.insert(matrix, 0, pixel, axis=1)
        # Inserir zeros no final de todas as linhas do array
        matrix = numpy.insert(matrix, matrix.shape[1], pixel, axis=1)

        # Criar uma linha de zeros
        linha = numpy.zeros((1, matrix.shape[1], 3), numpy.uint8)
        # Inserir a linha de zeros no inicio
        matrix = numpy.insert(matrix, 0, linha, axis=0)
        # Inserir a linha de zeros no final
        matrix = numpy.insert(matrix, matrix.shape[0], linha, axis=0)

    return matrix


def mascara(image, mascara, linha, coluna, canal=-1):
    if len(image.shape) == 2:
        linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
        linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
        linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[6] + int(image[linha+1, coluna+1])*mascara[8]
        return linha01+linha02+linha03
    elif canal != -1:
        linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2]
        linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
        linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8]
        return linha01+linha02+linha03


def filtro_sobel_vertical(image):
    print("Result dimensions ", image.shape)
    # a = np.array([1, 4, 5, 8], float)
    # a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (-1, 0, 1, -2, 0, 2, -1, 0, 1)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
                linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
                linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[6] + int(image[linha+1, coluna+1])*mascara[8]
                result[linha-1, coluna-1] = abs(linha01+linha02+linha03)/4.0
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2]
                    linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8]
                    result[linha-1, coluna-1, canal] = abs(linha01+linha02+linha03)/4.0
    return result


def filtro_sobel_horizontal(image):
    print("Result dimensions ", image.shape)
    # a = np.array([1, 4, 5, 8], float)
    # a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (-1, -2, -1, 0, 0, 0, 1, 2, 1)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
                linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
                linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[7] + int(image[linha+1, coluna+1])*mascara[8]

                result[linha-1, coluna-1] = abs(linha01+linha02+linha03)/4.0
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8] 

                    result[linha-1, coluna-1, canal] = abs(linha01+linha02+linha03)/4.0
    return result


def filtro_sobel(image):
    print("Result dimensions ", image.shape)
    sobel_vertical = filtro_sobel_vertical(image)
    sobel_horizontal = filtro_sobel_horizontal(image)

    return image_add_01(sobel_vertical, sobel_horizontal)


def filtro_prewitt_vertical(image):
    print("Result dimensions ", image.shape)
    # a = np.array([1, 4, 5, 8], float)
    # a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (-1, 0, 1, -1, 0, 1, -1, 0, 1)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
                linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
                linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[6] + int(image[linha+1, coluna+1])*mascara[8]
                result[linha-1, coluna-1] = abs(linha01+linha02+linha03)/3.0
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2]
                    linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8]
                    result[linha-1, coluna-1, canal] = abs(linha01+linha02+linha03)/3.0
    return result


def filtro_prewitt_horizontal(image):
    print("Result dimensions ", image.shape)
    # a = np.array([1, 4, 5, 8], float)
    # a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (-1, -1, -1, 0, 0, 0, 1, 1, 1)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
                linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
                linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[7] + int(image[linha+1, coluna+1])*mascara[8]

                result[linha-1, coluna-1] = abs(linha01+linha02+linha03)/3.0
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2]
                    linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8]

                    result[linha-1, coluna-1, canal] = abs(linha01+linha02+linha03)/3.0
    return result


def filtro_prewitt(image):
    print("Result dimensions ", image.shape)
    prewitt_vertical = filtro_prewitt_vertical(image)
    prewitt_horizontal = filtro_prewitt_horizontal(image)

    return image_add_01(prewitt_vertical, prewitt_horizontal)


def filtro_roberts_vertical(image):
    print("Result dimensions ", image.shape)
    # a = np.array([1, 4, 5, 8], float)
    # a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (0, 0, -1, 0, 1, 0, 0, 0, 0)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
                linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
                linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[6] + int(image[linha+1, coluna+1])*mascara[8]
                result[linha-1, coluna-1] = abs(linha01+linha02+linha03)
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2]
                    linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8]
                    result[linha-1, coluna-1, canal] = abs(linha01+linha02+linha03)
    return result


def filtro_roberts_horizontal(image):
    print("Result dimensions ", image.shape)
    # a = np.array([1, 4, 5, 8], float)
    # a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (-1, 0, 0, 0, 1, 0, 0, 0, 0)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
                linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
                linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[7] + int(image[linha+1, coluna+1])*mascara[8]

                result[linha-1, coluna-1] = abs(linha01+linha02+linha03)
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2]
                    linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8]

                    result[linha-1, coluna-1, canal] = abs(linha01+linha02+linha03)
    return result


def filtro_roberts(image):
    print("Result dimensions ", image.shape)
    roberts_vertical = filtro_roberts_vertical(image)
    roberts_horizontal = filtro_roberts_horizontal(image)
    return image_add_01(roberts_vertical, roberts_horizontal)


def filtro_isotropico_vertical(image):
    print("Result dimensions ", image.shape)
    # a = np.array([1, 4, 5, 8], float)
    # a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (1, 0, -1, 1.4142135623730951, 0, -1.4142135623730951, 1, 0, -1)
    # div = 1
    # div = 1.5
    div = 3.414213562
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
                linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
                linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[6] + int(image[linha+1, coluna+1])*mascara[8]
                result[linha-1, coluna-1] = abs(linha01+linha02+linha03)/div
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8] 
                    result[linha-1, coluna-1, canal] = abs(linha01+linha02+linha03)/div
    return result


def filtro_isotropico_horizontal(image):
    print("Result dimensions ", image.shape)
    # a = np.array([1, 4, 5, 8], float)
    # a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (-1, -1.4142135623730951, -1, 0, 0, 0, 1, 1.4142135623730951, 1)
    # div = 1
    # div = 0.292893219
    # div = 1.292893219
    div = 3.414213562
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                linha01 = int(image[linha-1, coluna-1])*mascara[0] + int(image[linha-1, coluna])*mascara[1] + int(image[linha-1, coluna+1])*mascara[2]
                linha02 = int(image[linha, coluna-1])*mascara[3]   + int(image[linha, coluna])*mascara[4]   + int(image[linha, coluna+1])*mascara[5]
                linha03 = int(image[linha+1, coluna-1])*mascara[6] + int(image[linha+1, coluna])*mascara[7] + int(image[linha+1, coluna+1])*mascara[8]

                result[linha-1, coluna-1] = abs(linha01+linha02+linha03)/div
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    linha01 = int(image[linha-1, coluna-1, canal])*mascara[0] + int(image[linha-1, coluna, canal])*mascara[1]  + int(image[linha-1, coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha, coluna-1, canal])*mascara[3]   + int(image[linha, coluna, canal])*mascara[4]    + int(image[linha, coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1, coluna-1, canal])*mascara[6] + int(image[linha+1, coluna, canal])*mascara[7]  + int(image[linha+1, coluna+1, canal])*mascara[8] 

                    result[linha-1, coluna-1, canal] = abs(linha01+linha02+linha03)/div
    return result


def filtro_isotropico(image):
    print("Result dimensions ", image.shape)
    isotropico_vertical = filtro_isotropico_vertical(image)
    isotropico_horizontal = filtro_isotropico_horizontal(image)
    return image_add_01(isotropico_vertical, isotropico_horizontal)

if (__name__=='__main__i'):
    image = rosa_c
    cv2.imshow('Image', image)
    cv2.imshow('Filtro isotropico - horizontal', filtro_isotropico_horizontal(image))
    cv2.imshow('Filtro isotropico - vertical', filtro_isotropico_vertical(image))
    cv2.imshow('Isotropico - horizontal + vertical', filtro_isotropico(image))
    cv2.waitKey(0)

if (__name__=='__main__r'):
    image = bio_01
    cv2.imshow('Image', image)
    cv2.imshow('Filtro roberts - horizontal', filtro_roberts_horizontal(image))
    cv2.imshow('Filtro roberts - vertical', filtro_roberts_vertical(image))
    cv2.imshow('Roberts - horizontal + vertical', filtro_roberts(image))
    cv2.waitKey(0)

if (__name__=='__main__p'):
    image = rosa
    cv2.imshow('Image', image)
    cv2.imshow('Filtro prewitt - horizontal', filtro_prewitt_horizontal(image))
    cv2.imshow('Filtro prewitt - vertical', filtro_prewitt_vertical(image))
    cv2.imshow('Prewitt - horizontal + vertical', filtro_prewitt(image))
    cv2.waitKey(0)

if (__name__=='__main__s'):
    image = dragonite
    cv2.imshow('Image', image)
    cv2.imshow('Filtro sobel - horizontal', filtro_sobel_horizontal(image))
    cv2.imshow('Filtro sobel - vertical', filtro_sobel_vertical(image))
    cv2.imshow('Sobel - horizontal + vertical', filtro_sobel(image))
    cv2.waitKey(0)

if (__name__=='__main__'):
    image = coin
    cv2.imshow('Image', image)
    cv2.imshow('Sobel', filtro_sobel(image))
    cv2.imshow('Prewitt', filtro_prewitt(image))
    cv2.imshow('Roberts', filtro_roberts(image))
    cv2.imshow('Isotropico', filtro_isotropico(image))
    cv2.waitKey(0)
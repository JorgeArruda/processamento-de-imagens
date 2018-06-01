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

bio = cv2.imread('Imagens/bio01.png')
bio_c = cv2.imread('Imagens/bio01.png', cv2.IMREAD_GRAYSCALE)

bird = cv2.imread('Imagens/bird.png')
bird_c = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)

dragonite = cv2.imread('Imagens/dragonite.png')
dragonite_c = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)

rosa = cv2.imread('Imagens/rosa.png')
rosa_c = cv2.imread('Imagens/rosa.png', cv2.IMREAD_GRAYSCALE)

girl = cv2.imread('Imagens/girl1.png')
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


def apply_mascara(image, mascara, linha, coluna, canal=-1):
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


def filtro(image, mascara, div):
    if type(mascara) != tuple or not(type(div) != float or type(div) != int):
            return
    if len(mascara) != 9:
        return
    div = float(div)

    print("Result dimensions ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                new_pixel = apply_mascara(image, mascara, linha, coluna)
                result[linha-1, coluna-1] = abs(new_pixel)/div
    else:
        result = numpy.zeros((image.shape[0]-2, image.shape[1]-2, image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                for canal in range(0, image.shape[2]):
                    new_pixel = apply_mascara(image, mascara, linha, coluna, canal)
                    result[linha-1, coluna-1, canal] = abs(new_pixel)/div
    return result


def filtro_sobel(image, orientation='vertical ou horizontal'):
    print("Result dimensions ", image.shape)
    mascara_vertical = (-1, 0, 1, -2, 0, 2, -1, 0, 1)
    mascara_horizontal = (-1, -2, -1, 0, 0, 0, 1, 2, 1)

    if orientation == 'vertical':
        return filtro(image, mascara_vertical, 4.0)
    elif orientation == 'horizontal':
        return filtro(image, mascara_horizontal, 4.0)

    sobel_vertical = filtro(image, mascara_vertical, 4.0)
    sobel_horizontal = filtro(image, mascara_horizontal, 4.0)
    return image_add_01(sobel_vertical, sobel_horizontal)


def filtro_prewitt(image, orientation='vertical ou horizontal'):
    print("Result dimensions ", image.shape)
    mascara_vertical = (-1, 0, 1, -1, 0, 1, -1, 0, 1)
    mascara_horizontal = (-1, -1, -1, 0, 0, 0, 1, 1, 1)

    if orientation == 'vertical':
        return filtro(image, mascara_vertical, 3.0)
    elif orientation == 'horizontal':
        return filtro(image, mascara_horizontal, 3.0)

    prewitt_vertical = filtro(image, mascara_vertical, 3.0)
    prewitt_horizontal = filtro(image, mascara_horizontal, 3.0)
    return image_add_01(prewitt_vertical, prewitt_horizontal)


def filtro_roberts(image, orientation='vertical ou horizontal'):
    print("Result dimensions ", image.shape)
    mascara_vertical = (0, 0, -1, 0, 1, 0, 0, 0, 0)
    mascara_horizontal = (-1, 0, 0, 0, 1, 0, 0, 0, 0)

    if orientation == 'vertical':
        return filtro(image, mascara_vertical, 3.0)
    elif orientation == 'horizontal':
        return filtro(image, mascara_horizontal, 3.0)

    roberts_vertical = filtro(image, mascara_vertical, 3.0)
    roberts_horizontal = filtro(image, mascara_horizontal, 3.0)
    return image_add_01(roberts_vertical, roberts_horizontal)


def filtro_isotropico(image, orientation='vertical ou horizontal'):
    print("Result dimensions ", image.shape)
    mascara_vertical = (1, 0, -1, 1.4142135623730951, 0, -1.4142135623730951, 1, 0, -1)
    mascara_horizontal = (-1, -1.4142135623730951, -1, 0, 0, 0, 1, 1.4142135623730951, 1)
    # div = 1
    # div = 1.5
    div = 3.414213562

    if orientation == 'vertical':
        return filtro(image, mascara_vertical, div)
    elif orientation == 'horizontal':
        return filtro(image, mascara_horizontal, div)

    isotropico_vertical = filtro(image, mascara_vertical, div)
    isotropico_horizontal = filtro(image, mascara_horizontal, div)
    return image_add_01(isotropico_vertical, isotropico_horizontal)


if (__name__ == '__main__i'):
    image = rosa_c
    cv2.imshow('Image', image)
    cv2.imshow('Filtro isotropico - horizontal', filtro_isotropico(image, 'horizontal'))
    cv2.imshow('Filtro isotropico - vertical', filtro_isotropico(image, 'vertical'))
    cv2.imshow('Isotropico - horizontal + vertical', filtro_isotropico(image))
    cv2.waitKey(0)

if (__name__ == '__main__r'):
    image = bio
    cv2.imshow('Image', image)
    cv2.imshow('Filtro roberts - horizontal', filtro_roberts(image, 'horizontal'))
    cv2.imshow('Filtro roberts - vertical', filtro_roberts(image, 'vertical'))
    cv2.imshow('Roberts - horizontal + vertical', filtro_roberts(image))
    cv2.waitKey(0)

if (__name__ == '__main__p'):
    image = rosa
    cv2.imshow('Image', image)
    cv2.imshow('Filtro prewitt - horizontal', filtro_prewitt(image, 'horizontal'))
    cv2.imshow('Filtro prewitt - vertical', filtro_prewitt(image, 'vertical'))
    cv2.imshow('Prewitt - horizontal + vertical', filtro_prewitt(image))
    cv2.waitKey(0)

if (__name__ == '__main__s'):
    image = dragonite
    cv2.imshow('Image', image)
    cv2.imshow('Filtro sobel - horizontal', filtro_sobel(image, 'horizontal'))
    cv2.imshow('Filtro sobel - vertical', filtro_sobel(image, 'vertical'))
    cv2.imshow('Sobel - horizontal + vertical', filtro_sobel(image))
    cv2.waitKey(0)

if (__name__ == '__main__'):
    image = coin
    cv2.imshow('Image', image)
    cv2.imshow('Sobel', filtro_sobel(image))
    cv2.imshow('Prewitt', filtro_prewitt(image))
    cv2.imshow('Roberts', filtro_roberts(image))
    cv2.imshow('Isotropico', filtro_isotropico(image))
    cv2.waitKey(0)

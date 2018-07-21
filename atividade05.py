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

bio = cv2.imread('Imagens/bio01.png')
bio_c = cv2.imread('Imagens/bio01.png', cv2.IMREAD_GRAYSCALE)

gray = cv2.imread('Imagens/gray300.png', cv2.IMREAD_GRAYSCALE)

bird = cv2.imread('Imagens/bird.png')
bird_c = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)

dragonite = cv2.imread('Imagens/dragonite.png')
dragonite_c = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)

rosa = cv2.imread('Imagens/rosa1.png')
rosa_c = cv2.imread('Imagens/rosa1.png', cv2.IMREAD_GRAYSCALE)

girl = cv2.imread('Imagens/girl1.png')
girl_c = cv2.imread('Imagens/girl1.png', cv2.IMREAD_GRAYSCALE)

coin = cv2.imread('Imagens/coins.jpg')
coin_c = cv2.imread('Imagens/coins.jpg', cv2.IMREAD_GRAYSCALE)


def dithering_basico(image, lessgreater=[0, 255], limiar=127):
    print("Image dimensions ", image.shape)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0], image.shape[1]), numpy.uint8)
        for linha in range(1, image.shape[0]):
            for coluna in range(1, image.shape[1]):
                result[linha, coluna] = lessgreater[0] if image[linha, coluna] <= limiar else lessgreater[1]
    else:
        result = numpy.zeros((image.shape[0], image.shape[1], image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]):
            for coluna in range(1, image.shape[1]):
                for canal in range(0, image.shape[2]):
                    result[linha, coluna, canal] = lessgreater[0] if image[linha, coluna, canal] <= limiar else lessgreater[1]
    return result


def dithering_random(image, rangee=(-100, 0)):
    print("Image dimensions ", image.shape)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0], image.shape[1]), numpy.uint8)
        for linha in range(1, image.shape[0]):
            for coluna in range(1, image.shape[1]):
                result[linha, coluna] = 0 if (image[linha, coluna]+random.randrange(rangee[0], rangee[1])) <= 127 else 255
    else:
        result = numpy.zeros((image.shape[0], image.shape[1], image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]):
            for coluna in range(1, image.shape[1]):
                for canal in range(0, image.shape[2]):
                    result[linha, coluna, canal] = 0 if (image[linha, coluna, canal]+random.randrange(rangee[0], rangee[1])) <= 127 else 255
    return result


def dithering_periodico(image):
    print("Image dimensions ", image.shape)

    if len(image.shape) == 2:
        result = numpy.array(image)
        for linha in range(1, image.shape[0]):
            for coluna in range(1, image.shape[1]):
                i = linha % 3
                j = coluna % 3
                if (image[linha, coluna] > image[i, j]):
                    result[linha, coluna] = 0
                else:
                    result[linha, coluna] = 255
    else:
        result = numpy.zeros((image.shape[0], image.shape[1], image.shape[2]), numpy.uint8)
        for linha in range(1, image.shape[0]):
            for coluna in range(1, image.shape[1]):
                for canal in range(0, image.shape[2]):
                    i = linha % 3
                    j = coluna % 3
                    if (image[linha, coluna, canal] > image[i, j, canal]):
                        result[linha, coluna, canal] = 0
                    else:
                        result[linha, coluna] = 255
    return result


def dithering_aperiodico(image):
    print("Image dimensions ", image.shape)
    black = 0
    white = 255
    threshold = (black+white)/2
    if len(image.shape) == 2:
        result = numpy.array(image)
        for linha in range(1, image.shape[0]-1):
            for coluna in range(1, image.shape[1]-1):
                if (image[linha, coluna] < threshold):
                    result[linha, coluna] = black
                else:
                    result[linha, coluna] = white
                error = float(image[linha, coluna]) - float(result[linha, coluna])
                # image[linha+1, coluna] +=   int((7.0/16.0)*error)
                # image[linha, coluna+1] +=   int((5.0/16.0)*error)
                # image[linha+1, coluna+1] += int((1.0/16.0)*error)
                # image[linha+1, coluna-1] += int((3.0/16.0)*error)
                image[linha+1, coluna] +=   int((3.0/8.0)*error)
                image[linha, coluna+1] +=   int((3.0/8.0)*error)
                image[linha+1, coluna+1] += int((2.0/8.0)*error)
    return result


if (__name__ == '__main__'):
    # image = rosa
    # cv2.imshow('Image', image)

    image = rosa_c
    cv2.imshow('Image', image)
    # cv2.imshow('Dithering basico', dithering_basico(image))
    # cv2.imshow('Dithering aleatorio', dithering_random(image))
    # cv2.imshow('Dithering periodico', dithering_periodico(image))
    # cv2.imshow('Dithering aperiodico', dithering_aperiodico(image))
    cv2.waitKey(0)

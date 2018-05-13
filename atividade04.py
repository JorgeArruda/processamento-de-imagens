#!/usr/bin/env python3
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

def filtro_sobel_vertical(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (-1,0,1, -2,0,2, -1,0,1)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = abs(linha01+linha02+linha03)
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = abs(linha01+linha02+linha03)
    return result

def filtro_sobel_horizontal(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (-1,-2,-1, 0,0,0, 1,2,1)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[7] + int(image[linha+1,coluna+1])*mascara[8]
                
                result[linha-1,coluna-1] = abs(linha01+linha02+linha03)
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    
                    result[linha-1,coluna-1,canal] = abs(linha01+linha02+linha03)
    return result

def filtro_prewitt_vertical(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (-1,0,1, -1,0,1, -1,0,1)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = abs(linha01+linha02+linha03)/3
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = abs(linha01+linha02+linha03)/3
    return result

def filtro_prewitt_horizontal(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (-1,-1,-1, 0,0,0, 1,1,1)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[7] + int(image[linha+1,coluna+1])*mascara[8]
                
                result[linha-1,coluna-1] = abs(linha01+linha02+linha03)/3
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    
                    result[linha-1,coluna-1,canal] = abs(linha01+linha02+linha03)/3
    return result


def filtro_roberts_vertical(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (0,0,-1, 0,1,0, 0,0,0)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = abs(linha01+linha02+linha03)
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = abs(linha01+linha02+linha03)
    return result

def filtro_roberts_horizontal(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (-1,0,0, 0,1,0, 0,0,0)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[7] + int(image[linha+1,coluna+1])*mascara[8]
                
                result[linha-1,coluna-1] = abs(linha01+linha02+linha03)
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    
                    result[linha-1,coluna-1,canal] = abs(linha01+linha02+linha03)
    return result

def filtro_isotropico_vertical(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (1,0,-1, 1.4142135623730951,0,-1.4142135623730951, 1,0,-1)
    # div = 1
    div = 0.292893219
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = math.floor(abs(linha01+linha02+linha03)/div)
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = math.floor(abs(linha01+linha02+linha03)/div)
    return result

def filtro_isotropico_horizontal(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (-1,-1.4142135623730951,-1, 0,0,0, 1,1.4142135623730951,1)
    # div = 1
    div = 0.292893219
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[7] + int(image[linha+1,coluna+1])*mascara[8]
                
                result[linha-1,coluna-1] = math.floor(abs(linha01+linha02+linha03)/div)
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    
                    result[linha-1,coluna-1,canal] = math.floor(abs(linha01+linha02+linha03)/div)
    return result


if (__name__=='__main__s'):
    # cv2.imshow('Image', bio_01)
    # horizontal = filtro_sobel1(filtro_gaussiano(filtro_gaussiano(filtro_gaussiano(bio_01))))
    # cv2.imshow('Filtro sobel horizontal - ----------', horizontal)
    # vertical = filtro_sobel2(filtro_gaussiano(bio_01))
    # cv2.imshow('Filtro sobel vertical - ----------', vertical)
    # sobel = image_add_01(horizontal, vertical)
    # cv2.imshow('Sobel normalizada - horizontal + vertical', sobel)

    # sobel = image_add_01(bio_01, sobel)
    # cv2.imshow('Sobel - horizontal * vertical', sobel)
    # sobel2 = image_add(horizontal, bio_01)
    # cv2.imshow('Filtro - horizontal + image', sobel2)
    # sobel3 = image_add(bio_01, vertical)
    # cv2.imshow('Filtro sobel - image + vertical', sobel3)
    # sobel4 = image_add(bio_01, sobel)
    # cv2.imshow('Filtro sobel - image + (horizontal + vertical)', sobel4)
    # filtro_sobel(foto_02)
    cv2.waitKey(0)

if (__name__=='__main__p'):
    cv2.imshow('Image', bio_01)
    horizontal = filtro_prewitt_horizontal(filtro_gaussiano(bio_01))
    cv2.imshow('Filtro prewitt - horizontal', horizontal)
    vertical = filtro_prewitt_vertical(filtro_gaussiano(bio_01))
    cv2.imshow('Filtro prewitt - vertical', vertical)
    sobel = image_add_01(horizontal, vertical)
    cv2.imshow('Prewitt normalizado - horizontal + vertical', sobel)
    cv2.waitKey(0)

if (__name__=='__main__r'):
    cv2.imshow('Image', bio_01)
    horizontal = filtro_roberts_horizontal(filtro_gaussiano(bio_01))
    cv2.imshow('Filtro roberts - horizontal', horizontal)
    vertical = filtro_roberts_vertical(filtro_gaussiano(bio_01))
    cv2.imshow('Filtro roberts - vertical', vertical)
    sobel = image_add_01(horizontal, vertical)
    cv2.imshow('roberts normalizado - horizontal + vertical', sobel)
    cv2.waitKey(0)

if (__name__=='__main__'):
    cv2.imshow('Image', bio_01)
    horizontal = filtro_isotropico_horizontal(filtro_gaussiano(bio_01))
    cv2.imshow('Filtro isotropico - horizontal', horizontal)
    vertical = filtro_isotropico_vertical(filtro_gaussiano(bio_01))
    cv2.imshow('Filtro isotropico - vertical', vertical)
    sobel = image_add_01(horizontal, vertical)
    cv2.imshow('isotropico normalizado - horizontal + vertical', sobel)
    cv2.waitKey(0)
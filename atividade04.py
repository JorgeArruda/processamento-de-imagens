#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Atividade 02 Histograma
import numpy
from cv2 import cv2
from atividade01 import image_add_01, image_add

# Atividade 04 Realce de bordas:
#     - Sobel          
#     - Prewitt           
#     - Roberts            
#     - Isotrópico 

foto_01 = cv2.imread('Imagens/foto01.png')
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

def filtro_sobel(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (-1,0,1, -2,0,2, -1,0,1)
    gradienteX = ( mascara[7]+mascara[8] ) - ( mascara[4]+mascara[5] )
    gradienteY = ( mascara[5]+mascara[8] ) - ( mascara[4]+mascara[7] )
    gradiente = abs(gradienteX) + abs(gradienteY)
    print("gradiente", gradiente)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = (linha01+linha02+linha03)/gradiente
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = (linha01+linha02+linha03)/gradiente
    
    cv2.imshow('Imagem', image)
    cv2.imshow('Filtro sobel horizontal - ----------', result)
    cv2.waitKey(0)
    return result

def filtro_sobel2(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    mascara = (-1,-2,-1, 0,0,0, 1,2,1)
    gradienteX = ( mascara[7]+mascara[8] ) - ( mascara[4]+mascara[5] )
    gradienteY = ( mascara[5]+mascara[8] ) - ( mascara[4]+mascara[7] )
    gradiente = abs(gradienteX) + abs(gradienteY)
    print("gradiente", gradiente)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = (linha01+linha02+linha03)/gradiente
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = (linha01+linha02+linha03)/gradiente
    
    cv2.imshow('Imagem', image)
    cv2.imshow('Filtro sobel vertical - ----------', result)
    cv2.waitKey(0)
    return result

horizontal = filtro_sobel(bio_02)
vertical = filtro_sobel2(bio_02)
image_add(horizontal, vertical)
# filtro_sobel(foto_02)
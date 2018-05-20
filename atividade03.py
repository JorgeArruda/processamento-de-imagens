#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from cv2 import cv2
# Atividade 03 Convolução
# Jorge de Arruda Martins

bird = cv2.imread('Imagens/bird.png')
dragonite = cv2.imread('Imagens/dragonite.png')
bird_01 = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite_01 = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)
girl_gray = cv2.imread('Imagens/girl1.png', cv2.IMREAD_GRAYSCALE)
rosa_gray = cv2.imread('Imagens/rosa1.png', cv2.IMREAD_GRAYSCALE)
rosa = cv2.imread('Imagens/rosa1.png')

print('Bird   [Linhas, Colunas, Canais]: ', bird.shape)
print('Dragonite [Linhas, Colunas, Canais]: ', dragonite.shape)

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

def filtro_passabaixa(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)
    
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1]) + int(image[linha-1,coluna]) + int(image[linha-1,coluna+1])
                linha02 = int(image[linha,coluna-1])   + int(image[linha,coluna])   + int(image[linha,coluna+1])
                linha03 = int(image[linha+1,coluna-1]) + int(image[linha+1,coluna]) + int(image[linha+1,coluna+1])
                result[linha-1,coluna-1] = (linha01+linha02+linha03)/9
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal]) + int(image[linha-1,coluna, canal])  + int(image[linha-1,coluna+1, canal]) 
                    linha02 = int(image[linha,coluna-1, canal])   + int(image[linha,coluna, canal])    + int(image[linha,coluna+1, canal]) 
                    linha03 = int(image[linha+1,coluna-1, canal]) + int(image[linha+1,coluna, canal])  + int(image[linha+1,coluna+1, canal]) 
                    result[linha-1,coluna-1,canal] = (linha01+linha02+linha03)/9

    print(" Result ", result.shape)
    return result

def filtro_mediana(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                roll = [ image[linha-1,coluna-1], image[linha-1,coluna], image[linha-1,coluna+1], image[linha,coluna-1], image[linha,coluna], image[linha,coluna+1], image[linha+1,coluna-1], image[linha+1,coluna], image[linha+1,coluna+1] ]
                linha01 = int(image[linha-1,coluna-1]) + int(image[linha-1,coluna]) + int(image[linha-1,coluna+1])
                linha02 = int(image[linha,coluna-1])   + int(image[linha,coluna])   + int(image[linha,coluna+1])
                linha03 = int(image[linha+1,coluna-1]) + int(image[linha+1,coluna]) + int(image[linha+1,coluna+1])
                result[linha-1,coluna-1] = (linha01+linha02+linha03)/9 
                roll.sort() # Ordena a lista
                result[linha-1,coluna-1] = roll[4] # Mediana
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    roll = [ image[linha-1,coluna-1, canal], image[linha-1,coluna, canal] , image[linha-1,coluna+1, canal], image[linha,coluna-1, canal], image[linha,coluna, canal], image[linha,coluna+1, canal], image[linha+1,coluna-1, canal], image[linha+1,coluna, canal], image[linha+1,coluna+1, canal] ]
                    roll.sort() 
                    result[linha-1,coluna-1,canal] = roll[4]
    
    return result

def filtro_gaussiano(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    # print("\n Imagem(addZeros) ", image.shape)

    mascara = (1,2,1, 2,4,2, 1,2,1)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = (linha01+linha02+linha03)/16
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = (linha01+linha02+linha03)/16
    
    return result

def filtro_passaalta(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (-1,-1,-1, -1,1,-1, -1,-1,-1)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = (linha01+linha02+linha03)/9
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = (linha01+linha02+linha03)/9
    
    return result

def filtro_convolucao(image):
    print("Result dimensions ",image.shape)
    #a = np.array([1, 4, 5, 8], float)
    #a = a.reshape((5, 2))
    print(" Imagem ", image.shape)
    image = addZero(image)
    print("\n Imagem(addZeros) ", image.shape)

    mascara = (1,1,1, 1,1,1, 1,1,1)
    if len(image.shape) == 2:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                linha01 = int(image[linha-1,coluna-1])*mascara[0] + int(image[linha-1,coluna])*mascara[1] + int(image[linha-1,coluna+1])*mascara[2]
                linha02 = int(image[linha,coluna-1])*mascara[3]   + int(image[linha,coluna])*mascara[4]   + int(image[linha,coluna+1])*mascara[5]
                linha03 = int(image[linha+1,coluna-1])*mascara[6] + int(image[linha+1,coluna])*mascara[6] + int(image[linha+1,coluna+1])*mascara[8]
                result[linha-1,coluna-1] = (linha01+linha02+linha03)/9
    else:
        result = numpy.zeros((image.shape[0]-2,image.shape[1]-2,image.shape[2]), numpy.uint8)
        for linha in range(1,image.shape[0]-1):
            for coluna in range(1,image.shape[1]-1):
                for canal in range(0,image.shape[2]):
                    linha01 = int(image[linha-1,coluna-1, canal])*mascara[0] + int(image[linha-1,coluna, canal])*mascara[1]  + int(image[linha-1,coluna+1, canal])*mascara[2] 
                    linha02 = int(image[linha,coluna-1, canal])*mascara[3]   + int(image[linha,coluna, canal])*mascara[4]    + int(image[linha,coluna+1, canal])*mascara[5]
                    linha03 = int(image[linha+1,coluna-1, canal])*mascara[6] + int(image[linha+1,coluna, canal])*mascara[7]  + int(image[linha+1,coluna+1, canal])*mascara[8] 
                    result[linha-1,coluna-1,canal] = (linha01+linha02+linha03)/9
    return result
    

if (__name__ == '__main__'):
    image = bird
    cv2.imshow('Imagem', image)
    cv2.imshow('Imagem - Passa-alta',filtro_passaalta(image))
    cv2.waitKey(0)
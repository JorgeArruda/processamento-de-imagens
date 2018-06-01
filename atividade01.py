#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from cv2 import cv2
from atividade05 import dithering_basico
from atividade06 import segmentar_iterativo
# Atividade 01 Operações
# Jorge de Arruda Martins

bird_gray = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite_gray = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)
bird = cv2.imread('Imagens/bird.png')
dragonite = cv2.imread('Imagens/dragonite.png')
girl = cv2.imread('Imagens/girl1.png')
rosa = cv2.imread('Imagens/rosa1.png')
text = cv2.imread('Imagens/text33.png')
circulo = cv2.imread('Imagens/circulo.png')
quadrado = cv2.imread('Imagens/quadrado.png')
girl_gray = cv2.imread('Imagens/girl1.png', cv2.IMREAD_GRAYSCALE)
rosa_gray = cv2.imread('Imagens/rosa1.png', cv2.IMREAD_GRAYSCALE)
text_gray = cv2.imread('Imagens/text33.png', cv2.IMREAD_GRAYSCALE)
circulo_gray = cv2.imread('Imagens/circulo.png', cv2.IMREAD_GRAYSCALE)
quadrado_gray = cv2.imread('Imagens/quadrado.png', cv2.IMREAD_GRAYSCALE)

def image_add(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print('Linhas: ', image01.shape[1],'  ',image02.shape[1])
        result = numpy.array(image01)
        
        if (len(image01.shape) > 2):
            for linha in range(0, image01.shape[0]):
                for coluna in range(0, image01.shape[1]): 
                    (b0, g0, r0) = image01[linha,coluna]
                    (b1, g1, r1) = image02[linha,coluna]
                    result[linha,coluna] = ( 255 if b0+b1 > 255 else b0+b1, 255 if b0+b1 > 255 else g0+g1, 255 if b0+b1 > 255 else r0+r1)
            return result
        else:
            for linha in range(0, image01.shape[0]):
                for coluna in range(0, image01.shape[1]): 
                    a = image01[linha,coluna]
                    b = image02[linha,coluna]
                    result[linha,coluna] = 255 if a+b > 255 else a+b
            return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_add_01(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        # Quantidade de canais
        if len(image01.shape) != len(image02.shape):
            print('\nError - As imagens não possuem quantidades iguais de canais de cor')
            return image01
        if len(image01.shape) == 2:
            qtd_canais = 1
        else:
            qtd_canais = image01.shape[2]

        print('Linhas X Colunas: ', image01.shape[0],'  ',image02.shape[1])

        temp = []
        result = numpy.array(image01)

        max = []
        min = []
        for canal in range(qtd_canais):
            max.append(0)
            min.append(600)

        for linha in range(0,image01.shape[0]):
            temp.append([])
            for coluna in range(0,image01.shape[1]): 
                temp[linha].append([])
                for canal in range(0,qtd_canais): 
                    if qtd_canais <= 1:
                        temp[linha][coluna].append(int(image01[linha,coluna])+int(image02[linha,coluna]))
                    else:
                        temp[linha][coluna].append(int(image01[linha,coluna,canal])+int(image02[linha,coluna,canal]))
                    if temp[linha][coluna][canal] > max[canal]:
                        max[canal] = temp[linha][coluna][canal]
                    if temp[linha][coluna][canal] < min[canal]:
                        min[canal] = temp[linha][coluna][canal]
        constante = []
        for canal in range(qtd_canais):
            constante.append(255.0 / float(max[canal] - min[canal]))
        
        print('Matriz temporária - Max ', max,' - Min ', min,' Constante  ',constante,'\n')
        
        for linha in range(0,image01.shape[0]):
            for coluna in range(0,image01.shape[1]): 
                for canal in range(0,qtd_canais): 
                    #print 'constante[canal] * (temp[linha][coluna][canal] - min[canal])  ',constante[canal] * (temp[linha][coluna][canal] - min[canal])
                    if qtd_canais <= 1:
                        result[linha,coluna] = constante[canal] * (temp[linha][coluna][canal] - min[canal])
                    else:
                        result[linha,coluna,canal] = constante[canal] * (temp[linha][coluna][canal] - min[canal])
                
        return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_sub(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print('Linhas: ', image01.shape[1],'  ',image02.shape[1])
        result = numpy.array(image01)
        
        
        for linha in range(0, image01.shape[0]):
            for coluna in range(0, image01.shape[1]): 
                (b0, g0, r0) = image01[linha,coluna]
                (b1, g1, r1) = image02[linha,coluna]
                result[linha,coluna] = ( b0-b1 if b0-b1 >= 0 else 0, g0-g1 if g0-g1 >= 0 else 0, r0-r1 if r0-r1 >= 0 else 0)
        return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_sub_01(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        # Quantidade de canais
        if len(image01.shape) != len(image02.shape):
            print('\nError - As imagens não possuem quantidades iguais de canais de cor')
            return image01
        if len(image01.shape) == 2:
            qtd_canais = 1
        else:
            qtd_canais = image01.shape[2]

        print('Linhas X Colunas: ', image01.shape[0],'  ',image02.shape[1])

        #temp = [ [ [0] * image01.shape[2] ]  * image01.shape[1] ] * image01.shape[0] # array[num. de linhas][num. de colunas][num. de canais]
        temp = []
        result = numpy.array(image01)

        max = []
        min = []
        for canal in range(qtd_canais):
            max.append(0)
            min.append(600)

        for linha in range(0,image01.shape[0]):
            temp.append([])
            for coluna in range(0,image01.shape[1]): 
                temp[linha].append([])
                for canal in range(0,qtd_canais): 
                    if qtd_canais <= 1:
                        temp[linha][coluna].append(int(image01[linha,coluna])-int(image02[linha,coluna]))
                    else:
                        temp[linha][coluna].append(int(image01[linha,coluna,canal])-int(image02[linha,coluna,canal]))
                    if temp[linha][coluna][canal] > max[canal]:
                        max[canal] = temp[linha][coluna][canal]
                    if temp[linha][coluna][canal] < min[canal]:
                        min[canal] = temp[linha][coluna][canal]
        constante = []
        for canal in range(qtd_canais):
            constante.append(255.0 / float(max[canal] - min[canal]))
        
        print('Matriz temporária - Max ', max,' - Min ', min,' Constante  ',constante,'\n')
        
        for linha in range(0,image01.shape[0]):
            for coluna in range(0,image01.shape[1]): 
                for canal in range(0,qtd_canais): 
                    #print 'constante[canal] * (temp[linha][coluna][canal] - min[canal])  ',constante[canal] * (temp[linha][coluna][canal] - min[canal])
                    if qtd_canais <= 1:
                        result[linha,coluna] = constante[canal] * (temp[linha][coluna][canal] - min[canal])
                    else:
                        result[linha,coluna,canal] = constante[canal] * (temp[linha][coluna][canal] - min[canal])
        return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_mult(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print('Linhas: ', image01.shape[1],'  ',image02.shape[1])
        result = numpy.array(image01)
        
        for linha in range(0, image01.shape[0]):
            for coluna in range(0, image01.shape[1]): 
                (b0, g0, r0) = image01[linha,coluna]
                (b1, g1, r1) = image02[linha,coluna]
                result[linha,coluna] = ( (b0*b1)%256, (g0*g1)%256, (r0*r1)%256)
        return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_mult_escalar(image01, escalar):
    print('Linhas: ', image01.shape[1],'  ',image02.shape[1])
    result = numpy.array(image01)
    
    for linha in range(0, image01.shape[0]):
        for coluna in range(0, image01.shape[1]): 
            (b0, g0, r0) = image01[linha,coluna]
            result[linha,coluna] = ( (b0*escalar)%256, (g0*escalar)%256, (r0*escalar)%256)
    return result

def image_div(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print('Linhas: ', image01.shape[1],'  ',image02.shape[1])
        result = numpy.array(image01)
        
        for linha in range(0, image01.shape[0]):
            for coluna in range(0, image01.shape[1]): 
                b0 = 1 if image01[linha,coluna, 0] == 0 else image01[linha,coluna, 0] 
                g0 = 1 if image01[linha,coluna, 1] == 0 else image01[linha,coluna, 1]
                r0 = 1 if image01[linha,coluna, 2] == 0 else image01[linha,coluna, 2]
                b1 = 1 if image02[linha,coluna, 0] == 0 else image02[linha,coluna, 0]
                g1 = 1 if image02[linha,coluna, 1] == 0 else image02[linha,coluna, 1]
                r1 = 1 if image02[linha,coluna, 2] == 0 else image02[linha,coluna, 2]
                result[linha,coluna] = ( int(float(b0)/float(b1)), int(float(g0)/float(g1)), int(float(r0)/float(r1)))
        return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_div_escalar(image01, escalar):
    print('Linhas: ', image01.shape[1],'  ',image02.shape[1])
    result = numpy.array(image01)
    
    for linha in range(0, image01.shape[0]):
        for coluna in range(0, image01.shape[1]): 
            (b0, g0, r0) = image01[linha,coluna]
            result[linha,coluna] = ( b0/escalar, g0/escalar, r0/escalar)
    return result

def image_or(image01, image02, truefalse=[0, 255]):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print('Image 01: ', image01.shape)
        print('Image 02: ', image02.shape)
        result = numpy.array(image01)
        for linha in range(0, image01.shape[0]):
            for coluna in range(0, image01.shape[1]): 
                if ( (image01[linha,coluna]==0) or (image02[linha,coluna]==0)):
                    result[linha,coluna] = truefalse[0]
                else:
                    result[linha,coluna] = truefalse[1]
        return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_and(image01, imag2, truefalse=[0, 255]):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print('Image 01: ', image01.shape)
        print('Image 02: ', image02.shape)
        result = numpy.array(image01)
        for linha in range(0, image01.shape[0]):
            for coluna in range(0, image01.shape[1]): 
                if ( (image01[linha,coluna]==0) and (image02[linha,coluna]==0)):
                    result[linha,coluna] = truefalse[0]
                else:
                    result[linha,coluna] = truefalse[1]
        return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_xor(image01, image02, truefalse=[0, 255]):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print('Image 01: ', image01.shape)
        print('Image 02: ', image02.shape)
        result = numpy.array(image01)
        for linha in range(0, image01.shape[0]):
            for coluna in range(0, image01.shape[1]): 
                if ( not((image01[linha,coluna]==0) or (image02[linha,coluna]==0)) ):
                    result[linha,coluna] = truefalse[0]
                else:
                    result[linha,coluna] = truefalse[1]
        return result
    else:
        print('As imagens não possuem tamanhos iguais')
        return image01

def image_not(image, truefalse=[0, 255]):
    print('Image: ', image.shape)
    result = numpy.array(image)
    for linha in range(0, image.shape[0]):
        for coluna in range(0, image.shape[1]): 
            if ( not( (image[linha,coluna]==0) ) ):
                result[linha,coluna] = truefalse[0]
            else:
                result[linha,coluna] = truefalse[1]
    return result

if __name__=='__main__':
    lessgreater = [255, 0]
    lessgreater1 = [0, 255]
    # image01 = dithering_basico(rosa, lessgreater1)
    # image02 = segmentar_iterativo(circulo, lessgreater1)
    image01 = rosa
    image02 = quadrado
    cv2.imshow('Image 01', image01)
    cv2.imshow('Image 02', image02)

    result = image_mult_escalar(image01, 1.1)
    cv2.imshow('Image 01 * 1.1', result) 
    
    cv2.waitKey(0)
     

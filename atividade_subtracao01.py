#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Atividade 01 Operações aritméticas e lógicas - Subtração de Imagens
import numpy
import cv2
import sys


bird = cv2.imread('Imagens/bird.png')
dragonite = cv2.imread('Imagens/dragonite.png')
bird_01 = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite_01 = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)

print 'Bird   [Linhas, Colunas, Canais]: ', bird.shape
print 'Dragonite [Linhas, Colunas, Canais]: ', dragonite.shape

def image_sub_01(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print 'Linhas: ', image01.shape[1],'  ',image02.shape[1]
        result = numpy.array(image01)
        max_linha = image01.shape[0]
        max_coluna = image01.shape[1]
        cv2.imshow("Image01", image01) # Mostrar imagem
        cv2.imshow("Image02", image02) # Mostrar imagem
        for linha in range(0,max_linha):
            for coluna in range(0,max_coluna): 
                (b0, g0, r0) = image01[linha,coluna]
                (b1, g1, r1) = image02[linha,coluna]
                #print "Lin: ",linha," Colu: ",coluna, " (b0, g0, r0): ",(b0, g0, r0)," (b1, g1, r1): ",(b1, g1, r1)
                result[linha,coluna] = (b0-b1, g0-g1, r0-r1)

        cv2.imshow("Subtracao 01, loop", result) # Mostrar imagem
        cv2.waitKey(0)
        return result
    else:
        print 'As imagens não possuem tamanhos iguais'
        return image01

def image_sub_02(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        
        print "\n\n"
        print 'Linhas: ', image01.shape
        result = numpy.array(image01)
        max_linha = image01.shape[0]
        max_coluna = image01.shape[1]
        cv2.imshow("Image01", image01) # Mostrar imagem
        cv2.imshow("Image02", image02) # Mostrar imagem
        for linha in range(0,max_linha):
            for coluna in range(0,max_coluna): 
                (b0, g0, r0) = image01[linha,coluna]
                (b1, g1, r1) = image02[linha,coluna]
                b = int(b0) - int(b1)
                g = int(g0) - int(g1)
                r = int(r0) - int(r1)
                #print "Lin: ",linha," Colu: ",coluna, " (b0, g0, r0): ",(b0, g0, r0)," (b1, g1, r1): ",(b1, g1, r1)
                result[linha,coluna] = ( b if b >= 0 else 0, g if g >= 0 else 0, r if r >= 0 else 0)
                """if linha == coluna:
                    #print ("  ", result[linha,coluna], end='')
                    sys.stdout.write(" ")
                    sys.stdout.write(str(result[linha,coluna]))
                    sys.stdout.flush"""

        cv2.imshow("Subtracao_02, truncada", result) # Mostrar imagem
        cv2.waitKey(0)
        return result
    else:
        print 'As imagens não possuem tamanhos iguais'
        return image01

def image_sub_03(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        # Quantidade de canais
        if len(image01.shape) != len(image02.shape):
            print '\nError - As imagens não possuem quantidades iguais de canais de cor'
            return image01
        if len(image01.shape) == 2:
            qtd_canais = 1
        else:
            qtd_canais = image01.shape[2]

        print 'Linhas X Colunas: ', image01.shape[0],'  ',image02.shape[1]
        cv2.imshow("Image01", image01) # Mostrar imagem
        cv2.imshow("Image02", image02) # Mostrar imagem

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
        
        print 'Matriz temporária - Max ', max,' - Min ', min,' Constante  ',constante,'\n'#,temp
        
        for linha in range(0,image01.shape[0]):
            for coluna in range(0,image01.shape[1]): 
                for canal in range(0,qtd_canais): 
                    #print 'constante[canal] * (temp[linha][coluna][canal] - min[canal])  ',constante[canal] * (temp[linha][coluna][canal] - min[canal])
                    if qtd_canais <= 1:
                        result[linha,coluna] = constante[canal] * (temp[linha][coluna][canal] - min[canal])
                    else:
                        result[linha,coluna,canal] = constante[canal] * (temp[linha][coluna][canal] - min[canal])
                    

        cv2.imshow("Subtracao 03, normalizada", result) # Mostrar imagem
        cv2.waitKey(0)
        
        return result
    else:
        print 'As imagens não possuem tamanhos iguais'
        return image01

image_sub_02(dragonite,bird)
image_sub_03(dragonite,bird)
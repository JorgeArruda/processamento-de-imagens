#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Atividade 01 Operações
import numpy
import cv2

quadrado01 = cv2.imread('/home/jorge/Documents/a.Projetos/Python/processamento de imagens/quadrado01.png', cv2.IMREAD_GRAYSCALE)
circulo01 = cv2.imread('/home/jorge/Documents/a.Projetos/Python/processamento de imagens/circulo01.png', cv2.IMREAD_GRAYSCALE)
quadrado02 = cv2.imread('/home/jorge/Documents/a.Projetos/Python/processamento de imagens/quadrado01.png')
circulo02 = cv2.imread('/home/jorge/Documents/a.Projetos/Python/processamento de imagens/circulo01.png')
quadrado03 = cv2.imread('/home/jorge/Documents/a.Projetos/Python/processamento de imagens/quadrado03.png')
circulo03 = cv2.imread('/home/jorge/Documents/a.Projetos/Python/processamento de imagens/circulo03.png')
_20x20 = cv2.imread('/home/jorge/Documents/a.Projetos/Python/processamento de imagens/20x20.png')
_20y20 = cv2.imread('/home/jorge/Documents/a.Projetos/Python/processamento de imagens/20y20.png')

print 'quadrado01: ',quadrado01.shape
print 'circulo01: ',circulo01.shape
print '20x20: ',_20x20.shape
print '20y20: ',_20y20.shape

def image_add(image01, image02):
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
                result[linha,coluna] = ( 255 if b0+b1 > 255 else b0+b1, 255 if b0+b1 > 255 else g0+g1, 255 if b0+b1 > 255 else r0+r1)

        cv2.imshow("adicao:", result) # Mostrar imagem
        cv2.waitKey(0)
        return result
    else:
        print 'As imagens não possuem tamanhos iguais'
        return image01

def image_add1(image01, image02):
    if image01.shape[0] == image02.shape[0] and image01.shape[1] == image02.shape[1]:
        print 'Linhas X Colunas: ', image01.shape[0],'  ',image02.shape[1]
        cv2.imshow("Image01", image01) # Mostrar imagem
        cv2.imshow("Image02", image02) # Mostrar imagem

        #temp = [ [ [0] * image01.shape[2] ]  * image01.shape[1] ] * image01.shape[0] # array[num. de linhas][num. de colunas][num. de canais]
        temp = []
        result = numpy.array(image01)

        print '_20x20',image01
        max = [0,0,0]
        min = [600,600,600]

        for linha in range(0,image01.shape[0]):
            temp.append([])
            for coluna in range(0,image01.shape[1]): 
                temp[linha].append([])
                for canal in range(0,image01.shape[2]): 
                    temp[linha][coluna].append(int(image01[linha,coluna,canal])+int(image02[linha,coluna,canal]))
                    if temp[linha][coluna][canal] > max[canal]:
                        max[canal] = temp[linha][coluna][canal]
                    if temp[linha][coluna][canal] < min[canal]:
                        min[canal] = temp[linha][coluna][canal]

        print 'Matriz temporária - Max ', max,' - Min ', min,'\n',temp
        constante = [255 / (max[0] - min[0]), 255 / (max[1] - min[1]), 255 / (max[2] - min[2])]
        for linha in range(0,image01.shape[0]):
            for coluna in range(0,image01.shape[1]): 
                for canal in range(0,image01.shape[2]): 
                    result[linha,coluna,canal] = constante[canal] * (temp[linha][coluna][canal] - min[canal])

        cv2.imshow("adicao normalizada:", result) # Mostrar imagem
        cv2.waitKey(0)
        return result
    else:
        print 'As imagens não possuem tamanhos iguais'
        return image01

def image_sub(image01, image02):
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
                result[linha,coluna] = ( b0-b1 if b0-b1 >= 0 else 0, g0-g1 if g0-g1 >= 0 else 0, r0-r1 if r0-r1 >= 0 else 0)

        cv2.imshow("subtracao: image01 - image02 = ", result) # Mostrar imagem
        cv2.waitKey(0)
        return result
    else:
        print 'As imagens não possuem tamanhos iguais'
        return image01

def image_mult(image01, image02):
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
                result[linha,coluna] = ( (b0*b1)%256, (g0*g1)%256, (r0*r1)%256)

        cv2.imshow("image01 * image02", result) # Mostrar imagem
        cv2.waitKey(0)
        return result
    else:
        print 'As imagens não possuem tamanhos iguais'
        return image01

def image_div(image01, image02):
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
                result[linha,coluna] = ( b0/b1, g0/g1, r0/r1)

        cv2.imshow("image01 / image02", result) # Mostrar imagem
        cv2.waitKey(0)
        return result
    else:
        print 'As imagens não possuem tamanhos iguais'
        return image01
        
#image_add(circulo02,quadrado02)
#image_sub(circulo02,quadrado02)
#image_add(circulo03,quadrado03)
image_add1(_20x20,_20y20)
image_add(_20x20,_20y20)
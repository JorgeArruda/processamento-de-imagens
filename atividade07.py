#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from cv2 import cv2

from atividade02 import image_histograma
from atividade05 import dithering_basico, dithering_random

foto_01 = cv2.imread('Imagens/foto01.png', cv2.IMREAD_GRAYSCALE)
foto_02 = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)
text_01 = cv2.imread('Imagens/text1.png', cv2.IMREAD_GRAYSCALE)
text_02 = cv2.imread('Imagens/text2.png', cv2.IMREAD_GRAYSCALE)
text_03 = cv2.imread('Imagens/text3.jpg', cv2.IMREAD_GRAYSCALE)
bio_01 = cv2.imread('Imagens/bio01.png', cv2.IMREAD_GRAYSCALE)
bio_02 = cv2.imread('Imagens/bio02.png', cv2.IMREAD_GRAYSCALE)
bird = cv2.imread('Imagens/bird.png', cv2.IMREAD_GRAYSCALE)
dragonite = cv2.imread('Imagens/dragonite.png', cv2.IMREAD_GRAYSCALE)
rosa = cv2.imread('Imagens/rosa.png')
rosa_gray = cv2.imread('Imagens/rosa.png', cv2.IMREAD_GRAYSCALE)
girl = cv2.imread('Imagens/foto02.png')
girl_gray = cv2.imread('Imagens/foto02.png', cv2.IMREAD_GRAYSCALE)


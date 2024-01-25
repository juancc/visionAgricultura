"""Punto de partida ejercicio 1"""
import cv2
import numpy as np


W = 100
H = 100

im = np.zeros((W,H), np.uint8)
for i in range(W): im[i,i] = 255


def show_im(im):
    cv2.imshow('window', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


show_im(im)



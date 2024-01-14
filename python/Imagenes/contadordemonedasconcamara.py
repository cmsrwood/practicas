import cv2 as cv
import numpy as np
def ordenarpuntos(puntos):
    n_puntos=np.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist()
    y_order=sorted(n_puntos,key=lambda n_puntos:n_puntos[1])
    
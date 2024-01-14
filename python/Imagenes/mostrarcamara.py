import cv2 as cv
import numpy as np

capturavideo=cv.VideoCapture(0)
total=0
for i in range(101 ):
    total=i
    print(f"Procesando imagen... {total}%")
valorGauss=9
valorKernel=9
if not capturavideo.isOpened():
    print("No se ha encontrado ninguna camara")
    exit()
while True:
    tipocamara,camara=capturavideo.read()
    grises=cv.cvtColor(camara,cv.COLOR_BGR2GRAY)
    gauss=cv.GaussianBlur(grises,(valorGauss,valorGauss),0)
    canny=cv.Canny(gauss,60,100)
    
    kernel=np.ones((valorKernel,valorKernel),np.uint8)
    cierre=cv.morphologyEx(canny,cv.MORPH_CLOSE,kernel)
    
    contornos,jerarquia=cv.findContours(cierre.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(camara, contornos, -1, (0,0,255),3) 
    cv.imshow('Camara', camara)
    if cv.waitKey(1)==ord("q"):
        break
capturavideo.release()
cv.destroyAllWindows()
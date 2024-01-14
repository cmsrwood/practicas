import cv2 as cv
imagen=cv.imread('contorno.jpg')
gray=cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
_,umbral=cv.threshold(gray,100,255,cv.THRESH_BINARY)
contorno,jerarquia=cv.findContours(umbral,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)     
cv.drawContours(imagen,contorno,-1,(0,255,0),3)  
# MOSTRAR
cv.imshow('Hola',imagen)

cv.waitKey(0)
cv.destroyAllWindows()
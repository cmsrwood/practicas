import cv2 as cv
import numpy as np
import os

modelo='Fotos Dilan'
ruta1='C:/Users/Dell/Documents/GitHub/practicas/python/ReconocimientoFacial'
rutacompleta=ruta1+'/'+modelo
if not os.path.exists(rutacompleta):
    os.makedirs(rutacompleta)
else:
    pass
     
camara=cv.VideoCapture(0)
ruidos=cv.CascadeClassifier('C:/Users/Dell/Documents/GitHub/practicas/python/ReconocimientoFacial/data\haarcascade_frontalface_default.xml')
id=0
while True:
    respuesta,captura=camara.read()
    if respuesta==False:
        break
    grises=cv.cvtColor(captura,cv.COLOR_BGR2GRAY)
    cara=ruidos.detectMultiScale(grises,1.3,5)
    idcaptura=captura.copy()
    
    for (x,y,e1,e2) in cara: 
        cv.rectangle(captura,(x,y),(x+e1,y+e2),(0,255,0),2)
    cv.imshow("Resultado",captura)
    if cv.waitKey(1)==ord('q'):
        break
camara.release()
cv.destroyAllWindows()

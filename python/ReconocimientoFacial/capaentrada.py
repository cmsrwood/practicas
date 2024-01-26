import cv2 as cv
ruidos=cv.CascadeClassifier('C:/Users/Dell/Documents/GitHub/practicas/python/ReconocimientoFacial\haarcascade_frontalface_default.xml')
camara=cv.VideoCapture(0)
while True:
    _,captura=camara.read()
    grises=cv.cvtColor(captura,cv.COLOR_BGR2GRAY)
    cara=ruidos.detectMultiScale(grises,)
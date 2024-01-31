import cv2 as cv
import os
import numpy as np
dataruta='C:/Users/Dell/Documents/GitHub/practicas/python/ReconocimientoFacial/data'
listadata=os.listdir(dataruta)
ids=[]
rostrosData=[]
id=0
for fila in listadata:
    rutacompleta=dataruta+'/'+fila
    print('Iniciando lectura...')
    for archivo in os.listdir(rutacompleta):
        print('Imagenes',fila + '/' + archivo)
        ids.append(id)
        rostrosData.append(cv.imread(rutacompleta+'/'+archivo,cv.COLOR_BGR2GRAY))
    id+=1
entrenamientoEigenRecognizer=cv.face.EigenFaceRecognizer_create()
print('Iniciando el entrenamiento...espere', entrenamientoEigenRecognizer)
entrenamientoEigenRecognizer.train(rostrosData,np.array(ids))
entrenamientoEigenRecognizer.write('EntrenamientoEigenRecognizer.xml')
print('Entrenamiento concluido')
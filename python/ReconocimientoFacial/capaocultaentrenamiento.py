import cv2 as cv
import os
import numpy as np
from time import time
dataruta='C:/Users/Dell/Documents/GitHub/practicas/python/ReconocimientoFacial/data'
listadata=os.listdir(dataruta)
ids=[]
rostrosData=[]
id=0
tiempoinicial=time()
for fila in listadata:
    rutacompleta=dataruta+'/'+fila
    print('Iniciando lectura...')
    for archivo in os.listdir(rutacompleta):
        
        print('Imagenes',fila + '/' + archivo)
        
        ids.append(id)
        rostrosData.append(cv.imread(rutacompleta+'/'+archivo,cv.COLOR_BGR2GRAY))
        
    id+=1
    tiempofinaldelectura=time()
    tiempototaldelectura=tiempofinaldelectura-tiempoinicial
    print('Tiempo total de lectura: ' , tiempototaldelectura)
    
entrenamientoEigenRecognizer=cv.face.EigenFaceRecognizer_create()
print('Iniciando el entrenamiento...espere', entrenamientoEigenRecognizer)
entrenamientoEigenRecognizer.train(rostrosData,np.array(ids))
tiempofinalentrenamiento=time()
tiempototalentrenamiento=tiempofinalentrenamiento-tiempototaldelectura
print('Tiempo de entrenamiento total: ',tiempototalentrenamiento)
entrenamientoEigenRecognizer.write('EntrenamientoEigenRecognizer.xml')
print('Entrenamiento concluido')
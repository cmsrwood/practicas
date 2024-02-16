numeronotas=int(input("Digite el numero de notas: "))
suma=0
notas=[]
for i in range(numeronotas):
    notas.append(float(input(f"Ingrese numero de la nota {i+1}: ")))
    suma+=notas[i]
promedio=suma/numeronotas
print(f"Su promedio es: {promedio}")
    
    
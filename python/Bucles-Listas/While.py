import math
numero=int(input("Ingrese un numero: "))

while numero<0:
    print("Ingrese un numero positivo")
    numero=int(input("Vuelva a ingresar un numero positivo: "))
    
print(f"La raiz cuadrada de {numero} es: {math.sqrt(numero):.82f}")
    

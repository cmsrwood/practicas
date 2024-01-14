num1=int(input("Ingrese el 1er numero: "))
num2=int(input("Ingrese el 2do numero: "))

if num1%2==0 and num2%2==0:
    print(f"Ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(f"El primer numero ({num1}) es par")
    print(f"El segundo numero ({num2}) es impar")
elif num2%2==0 and num1%2!=0:
    print(f"El primer numero ({num1}) es impar")
    print(f"El segundo numero ({num2}) es par")
else:
    print("Ambos son impares")
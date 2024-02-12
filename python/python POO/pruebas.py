def nota(nota1,nota2,nota3,nota4):
    porcen=(nota1*0.2)+(nota2*0.2)+(nota3*0.1)+(nota4*0.5)
    print(f"Tu nota es {round(porcen,2)}")
nota1=int(input("Digite su 1ra nota: "))
nota2=int(input("Digite su 2da nota: "))
nota3=int(input("Digite su 3ra nota: "))
nota4=int(input("Digite su 4ta nota: "))
nota(nota1,nota2,nota3,nota4)
    
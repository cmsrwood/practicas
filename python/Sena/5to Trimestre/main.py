def entradas():    
    
    nombre = str(input("Ingrese su nombre: "))

    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
    while ano_nacimiento < 1900 or ano_nacimiento >= 2026:
        print("Año de nacimiento inválido")
        ano_nacimiento = int(input("Ingrese su año de nacimiento: "))

    mes_nacimiento = int(input("Ingrese su mes de nacimiento: "))
    while mes_nacimiento < 1 or mes_nacimiento > 12:
        print("Mes de nacimiento inválido")
        mes_nacimiento = int(input("Ingrese su mes de nacimiento: "))


    dia_nacimiento = int(input("Ingrese su dia de nacimiento: "))
    while dia_nacimiento < 1 or dia_nacimiento > 31:
        print("Dia de nacimiento inválido")
        dia_nacimiento = int(input("Ingrese su dia de nacimiento: "))

    ano_actual = int(input("Ingrese el año actual: "))
    while ano_actual < 1900 or ano_actual > 2025:
        print("Año actual inválido")
        ano_actual = int(input("Ingrese el año actual: "))


    mes_actual = int(input("Ingrese el mes actual: "))
    while mes_actual < 1 or mes_actual > 12:
        print("Mes actual inválido")
        mes_actual = int(input("Ingrese el mes actual: "))


    dia_actual = int(input("Ingrese el dia actual: "))
    while dia_actual < 1 or dia_actual > 31:
        print("Dia actual inválido")
        dia_actual = int(input("Ingrese el dia actual: "))
        
    return nombre, dia_nacimiento, mes_nacimiento, ano_nacimiento, dia_actual, mes_actual, ano_actual

def calcular_edad(nombre, dia_nacimiento, mes_nacimiento, ano_nacimiento, dia_actual, mes_actual, ano_actual):
    dia = dia_actual - dia_nacimiento
    meses = mes_actual - mes_nacimiento
    ano = ano_actual - ano_nacimiento
        
    if meses <= 0:
        meses += 12
        ano -= 1
            
    if dia <= 0:
        dia += 30
        meses -= 1

    return f"{nombre}, su edad es: {ano} años, {meses} meses y {dia} días"

def main ():
    nombre, dia_nacimiento, mes_nacimiento, ano_nacimiento, dia_actual, mes_actual, ano_actual = entradas()
    print(calcular_edad(nombre, dia_nacimiento, mes_nacimiento, ano_nacimiento, dia_actual, mes_actual, ano_actual))

if __name__ == "__main__":
    main()

def entradas():    
    
    nombre = str(input("Ingrese su nombre: "))
    dia_nacimiento = int(input("Ingrese su dia de nacimiento: "))
    mes_nacimiento = int(input("Ingrese su mes de nacimiento: "))
    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))

    dia_actual = int(input("Ingrese el dia actual: "))
    mes_actual = int(input("Ingrese el mes actual: "))
    ano_actual = int(input("Ingrese el año actual: "))
    
    if dia_nacimiento < 1 or dia_nacimiento > 31:
        print("Dia inválido")
    if mes_nacimiento < 1 or mes_nacimiento > 12:
        print("Mes inválido")
    if dia_actual < 1 or dia_actual > 31:
        print("Dia inválido")
    if mes_actual < 1 or mes_actual > 12:
        print("Mes inválido")
    if ano_actual < 1900 or ano_actual > 2025:
        print("Año inválido")
    if ano_nacimiento < 1900 or ano_nacimiento > 2025:
        print("Año inválido")
        
    return dia_nacimiento, mes_nacimiento, ano_nacimiento, dia_actual, mes_actual, ano_actual
    
def mesANombre(mes):
    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    
    return switcher.get(mes)

def calcular_edad(dia_nacimiento, mes_nacimiento, ano_nacimiento, dia_actual, mes_actual, ano_actual):
    dia = dia_actual - dia_nacimiento
    meses = mes_actual - mes_nacimiento
    ano = ano_actual - ano_nacimiento
        
    if meses < 0:
        meses += 12
        ano -= 1
            
    if dia < 0:
        dia += 30
        meses -= 1
        if meses < 0:
            meses += 12
            ano -= 1
    return f"Su edad es: {ano} años, {meses} meses y {dia} días"

def main ():
    dia_nacimiento, mes_nacimiento, ano_nacimiento, dia_actual, mes_actual, ano_actual = entradas()
    print(calcular_edad(dia_nacimiento, mes_nacimiento, ano_nacimiento, dia_actual, mes_actual, ano_actual))
    

if __name__ == "__main__":
    main()
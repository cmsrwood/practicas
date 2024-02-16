estado=str(input("Ingrese su estado (ayunas/posprandial): "))
glucosa=float(input("Ingrese su nivel de glucosa en mmol/l: "))
if estado =='ayunas':
    if glucosa <4.4:
        print("Usted tiene hipoglusemia")
    elif glucosa>4.4 and glucosa <6.1:
        print("No tienes diabetes")
    elif glucosa>6.1 and glucosa <7:
        print("Tienes pre diabetes")
    elif glucosa>=7:
        print("Tienes diabetes")
elif estado=='posprandial':
    if glucosa<7.8:
        print("No tienes diabetes")
    elif glucosa>7.8 and glucosa <11:
        print("Tienes pre diabetes")
    elif glucosa>=11:
        print("Tienes diabetes")
else:
    print("Error en los datos")
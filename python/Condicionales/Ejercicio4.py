saldo=2000
nombre=input("Escriba su nombre: ")
opcion=0
while opcion==0:
    opcion=int(input(f"------------------------MENU-------------------------\nHola {nombre}, su saldo es de ${saldo}\n1.Ingreso de dinero\n2.Retirar dinero\n3.Mostrar dinero\n4.Salir\nSu opcion: "))
    # INGRESO
    if opcion == 1:
        ingreso=float(input("Digite la cantidad de dinero que desea ingresar: "))
        saldo+=ingreso
        print(f"Su saldo actual es de ${saldo}")
        q=int(input("Si desea realizar otra transaccion digite 1, de lo contrario digite 2:\nSu opcion: "))
        while q!=1 and q!=2:
            q=int(input("El numero digitado no es valido, intentelo de nuevo: "))
        if q==1:
            opcion=0
        elif q==2:
            print("Gracias por usar nuestro cajero :)")
    # RETIRAR DINERO
    elif opcion == 2:
        retiro=float(input("Digite la cantidad de dinero que desea retirar: "))
        if retiro>saldo:
            print("Saldo insuficiente")
        else:
            saldo-=retiro
        print(f"Su saldo actual es de ${saldo}")
        q=int(input("Si desea realizar otra transaccion digite 1, de lo contrario digite 2:\nSu opcion: "))
        while q!=1 and q!=2:
            q=int(input("El numero digitado no es valido, intentelo de nuevo: "))
        if q==1:
            opcion=0
        elif q==2:
            print("Gracias por usar nuestro cajero :)")
            
    # MOSTRAR DINERO
    elif opcion == 3:
        print(f"Su saldo actual es de ${saldo}")
        q=int(input("Si desea realizar otra transaccion digite 1, de lo contrario digite 2:\nSu opcion: "))
        while q!=1 and q!=2:
            q=int(input("El numero digitado no es valido, intentelo de nuevo: "))
        if q==1:
            opcion=0
        elif q==2:
            print("Gracias por usar nuestro cajero :)")
    # 
    elif opcion == 4:
        print("Gracias por usar nuestro cajero :)")
    else:
        if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4: 
            print("Opcion no valida, intentelo de nuevo")
            opcion=0
c=float(input("Ingrese el valor del capital: "))
c_doble=c*2
print(f"El valor doble es: {c_doble}")
meses=0
while c<c_doble:  
    i=c*0.05
    c+=i
    meses+=1
    print(f"Mes #{meses}")
    print(f"{round(c,2)}\n")
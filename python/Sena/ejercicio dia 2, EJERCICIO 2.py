def grado_ef(t_d,t_p):
    if t_d>200 and t_p<10000:
        print("Grado 5")
    elif t_d<200 and t_p<10000:
        print("Grado 6")
    elif t_d>200 and t_p>10000:
        print("Grado 7")
    elif t_d<200 and t_p>10000:
        print("Grado 8")
        
defectuosos=int(input("ingrese el numero de tornillos defectuosos: "))
producidos=int(input("ingrese el numero de tornillos producidos: "))
grado_ef(defectuosos,producidos)
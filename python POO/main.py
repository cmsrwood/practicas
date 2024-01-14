import pygame as pg 
import sys
class personaje:

    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre= nombre
        self.fuerza= fuerza
        self.inteligencia= inteligencia
        self.defensa= defensa
        self.vida= vida 
        
    def atributos(self):
        print("Nombre: ",self.nombre)
        print("Fuerza: ",self.fuerza)
        print("Inteligencia: ",self.inteligencia)
        print("Defensa: ",self.defensa)
        print("Vida: ",self.vida)
        
    def subirnivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def estavivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida=0
        print("Rayos, se murió",self.nombre)
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar (self,enemigo):
        daño= self.daño(enemigo)
        enemigo.vida= enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a: ",enemigo.nombre)
        if enemigo.estavivo():
            print("La vida de", enemigo.nombre, "es: ",enemigo.vida)
        else:
            enemigo.morir()
            
    def getfuerza(self):
        return self.fuerza
    
    def setfuerza(self , fuerza):
        if fuerza < 0:
            print("No se puede hacer eso mi loko")
        else:
            self.fuerza = fuerza
    
class guerrero(personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    
    def cambiar_arma(self):
        opcion= int(input("Elige un arma: 1.Matapuercos daño 8\n2.Matadragones, daño 10\n Su opcion: "))
        if opcion==1:
            self.espada=8
        elif opcion==2:
            self.espada=10
        else:
            print("La opción no es valida")
            
    def atributos(self):
        super().atributos()
        print("Espada: ",self.espada)
    
    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
class mago(personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)    
        self.libro= libro

    def atributos(self):
        super().atributos()
        print("Libro: ", self.libro)
        
    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
    

personaje_1 = guerrero("Guts",20,10,4,100,4)
personaje_2 = mago("Moon",5,15,4,100,3)

def combate(jugador_1,jugador_2):
    turno=0
    while jugador_1.estavivo() and jugador_2.estavivo():
        print("\nTurno: ", turno,"\n")
        print(">>>Accion de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>>Accion de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno+=1
    if jugador_1.estavivo():
        print("\nHa ganado ",jugador_1.nombre)
    elif jugador_2.estavivo():
        print("\nHa ganado", jugador_2.nombre) 
    else:
        print("Empate")   
    
combate(personaje_1,personaje_2)
import pygame as pg 
from sys import exit

pg.init()
#variables#
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
#Clases
class personaje:
    def __init__(self,):
        pass
#Funcion de eventos# 
def events(): 
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                clock.tick()
while True:
    events()
    screen.fill("White")
    pg.display.update()
    clock.tick(60)
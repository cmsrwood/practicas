import pygame as pg 
import sys

pg.init()
pg.mixer.init()
#variables#

clock=pg.time.Clock()
fondo=pg.image.load('imagenes/fondo.png')
laser_sonido = pg.mixer.Sound('audios/laser.wav')
width=fondo.get_width()
height=fondo.get_height()
size=(width,height)
screen=pg.display.set_mode(size,pg.SCALED|pg.FULLSCREEN)    
#Clases
class Nave(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load('imagenes/nave.PNG').convert_alpha()
        pg.display.set_caption("Galaga falso")
        pg.display.set_icon(self.image)
        self.rect=self.image.get_rect()
        self.rect.centerx=width/2
        self.rect.centery=height-50
        self.velocidad_x=0
        self.velocidad_y=0
    def mover (self):
        self.rect.centerx += self.velocidad_x
        self.rect.centery += self.velocidad_y
    def disparar(self):
        bala=Balas(self.rect.centerx,self.rect.centery)
        grupo_jugador.add(bala)
        grupo_balas_jugador.add(bala)
        laser_sonido.play()
    def update(self):
        self.rect.x += self.velocidad_x
        if self.rect.right > width:
            self.rect.right = width
        elif self.rect.left < 0:
            self.rect.left = 0
class Balas(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('imagenes/bala.PNG').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.y=y
        self.velocidad = -10
    def mover(self):
        self.rect.y += self.velocidad
    def update(self):
        self.rect.y +=  self.velocidad
# JUGADOR
grupo_jugador=pg.sprite.Group()
grupo_balas_jugador=pg.sprite.Group()
jugador=Nave()
grupo_jugador.add(jugador)
grupo_balas_jugador.add(jugador)

#Funcion de eventos# 
def events(): 
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            # movimiento
            if event.key==pg.K_a:
                jugador.velocidad_x=-5
            if event.key==pg.K_d:
                jugador.velocidad_x=5
            # disparo
            if event.key==pg.K_SPACE:
                jugador.disparar()
        if event.type==pg.KEYUP:
            if event.key==pg.K_a:
                jugador.velocidad_x=0
            if event.key==pg.K_d:
                jugador.velocidad_x=0
def main():
    while True:
        screen.blit(fondo, (0,0))
        events()
        grupo_jugador.update()
        grupo_balas_jugador.update()
        grupo_jugador.draw(screen)
        jugador.mover()
        pg.display.update()
        clock.tick(60)
main()
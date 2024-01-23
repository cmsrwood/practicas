import pygame as pg, sys
pg.init()
BLACK = (0,0,0)
WHITE= (255,255,255)
RED = (255,0,0)
size = (800, 500)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
pg.mouse.set_visible(0)
#Coordenadas del cuadrado
x = 10
y = 10
#Velocidad
x_speed = 0
y_speed = 0
personaje=pg.image.load('juego python/personaje.jpg')
while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		#Eventos teclado
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_LEFT:
				x_speed = -3
			if event.key == pg.K_RIGHT:
				x_speed = 3
			if event.key == pg.K_UP:
				y_speed = -3
			if event.key == pg.K_DOWN:
				y_speed = 3
		if event.type == pg.KEYUP:
			if event.key == pg.K_LEFT:
				x_speed = 0
			if event.key == pg.K_RIGHT:
				x_speed = 0
			if event.key == pg.K_UP:
				y_speed = 0
			if event.key == pg.K_DOWN:
				y_speed = 0
	screen.fill(WHITE)
	x += x_speed
	y += y_speed
	screen.blit(personaje,[x,y])
	pg.display.flip()
	clock.tick(60)
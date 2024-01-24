import pygame as pg 
from sys import exit

pg.init()
#variables#
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
posicion_cancion=0
cambio=60
#fondos
tex_font = pg.font.Font(None,50)
tex_font2 = pg.font.Font(None,40)
fondo = pg.image.load('./imagenes/FONDO01.png').convert()
fondo_credito = pg.image.load('./imagenes/MENU/CREDITOS ROCK CLASS.png').convert()
fondo_menu=pg.image.load("./imagenes/MENU/BACKGROUN ROCK CLASS.png").convert_alpha()
posicion= (0,0)
barra_de_puntaje=pg.image.load("./imagenes/BARRA VS.png").convert_alpha()
boton1= pg.image.load('./imagenes/BOTONES/AZUL/01.png').convert_alpha()
posicion1= (50,450)
boton2= pg.image.load('./imagenes/BOTONES/NARANJA/01.png').convert_alpha()
posicion2= (150,450)
boton3= pg.image.load('./imagenes/BOTONES/ROJO/01.png').convert_alpha()
posicion3= (250,450)
boton4= pg.image.load('./imagenes/BOTONES/VERDE/01.png').convert_alpha()
posicion4= (460,450)
boton5= pg.image.load('./imagenes/BOTONES/AMARILLO/01.png').convert_alpha()
posicion5= (560,450)
boton6= pg.image.load('./imagenes/BOTONES/FUCCIA/01.png').convert_alpha()
posicion6= (660,450)

boton1_p= pg.image.load('./imagenes/BOTONES/AZUL/02.png').convert_alpha()
boton2_p= pg.image.load('./imagenes/BOTONES/NARANJA/02.png').convert_alpha()
boton3_p= pg.image.load('./imagenes/BOTONES/ROJO/02.png').convert_alpha()
boton4_p= pg.image.load('./imagenes/BOTONES/VERDE/02.png').convert_alpha()
boton5_p= pg.image.load('./imagenes/BOTONES/AMARILLO/02.png').convert_alpha()
boton6_p= pg.image.load('./imagenes/BOTONES/FUCCIA/02.png').convert_alpha()

nota1= pg.image.load('./imagenes/BOTONES/AZUL/03.png').convert_alpha()
nota2= pg.image.load('./imagenes/BOTONES/NARANJA/03.png').convert_alpha()
nota3= pg.image.load('./imagenes/BOTONES/ROJO/03.png').convert_alpha()
nota4= pg.image.load('./imagenes/BOTONES/VERDE/03.png').convert_alpha()
nota5= pg.image.load('./imagenes/BOTONES/AMARILLO/03.png').convert_alpha()
nota6= pg.image.load('./imagenes/BOTONES/FUCCIA/03.png').convert_alpha()
fuego=[]
for i in range(33):
    fuego.append(pg.image.load(f'./imagenes/fuego/{i}.png').convert_alpha())
anime_fuego=0
creditos=['Director artístico:','Santiago Troncoso Fernández','Jefe de Progrmadores:','Justo Soto M','Programadores:','Luna']
tex_credito=[]
po_credito= []
anime_credito= 0
credito_v = False
for h in creditos:
    tex_credito.append(tex_font2.render(h,True,'White'))

for h in range(len(tex_credito)):
    print(50*h)
    po_credito.append(tex_credito[h].get_rect(midtop=(400,600+(50*h))))


b1=False
b2=False
b3=False
b4=False
b5=False
b6=False
#canciones 
canciones=["smooth","I’m-So-Sorry","by-the-way"]
numero_cancion=0
pg.mixer.music.load(f"./audios/{canciones[numero_cancion]}.mp3")
error= pg.mixer.Sound(f"./sounds/error.wav")
error.set_volume(0.2)
Partitura=""
nota=""
play_song=False
lista_notas_0=[]
lista_notas_1=[]
lista_notas_2=[]
lista_notas_3=[]
lista_notas_4=[]
lista_notas_5=[]
centecimas=0
score_player_1 = 0
score_player_2 = 0
pg.mixer.music.play()
def music_time():
    tiempo=pg.time.get_ticks()/100
    return tiempo


#Funcion de eventos# 
time_Music=pg.USEREVENT +1
pg.time.set_timer(time_Music,100)
def events(): 
    global Partitura , nota , play_song , centecimas 
    global lista_notas_0,lista_notas_1,lista_notas_2,lista_notas_3, error
    global b1, b2, b3, b4, b5, b6
    global score_player_1, score_player_2, posicion_cancion
    global numero_cancion, cambio
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                pg.mixer.music.load(f"./audios/{canciones[numero_cancion]}.mp3")
                
                centecimas=music_time()
                Partitura=open(f"data_{canciones[0]}.txt", "r")
                play_song=True 
                nota=Partitura.readline()
                score_player_1=0
                score_player_2=0
                pg.mixer.music.play()
            if event.key==pg.K_UP:
                posicion_cancion +=1 
                numero_cancion +=1
                cambio=0
                if numero_cancion>= len(canciones):
                    numero_cancion=0
                pg.mixer.music.stop()
                pg.mixer.music.load(f"./audios/{canciones[numero_cancion]}.mp3")
                pg.mixer.music.play()
            if event.key==pg.K_DOWN:
                posicion_cancion -=1 
                numero_cancion -=1
                cambio=120
                if numero_cancion<0:
                    numero_cancion=len(canciones)-1
                
                pg.mixer.music.stop()
                pg.mixer.music.load(f"./audios/{canciones[numero_cancion]}.mp3")
                pg.mixer.music.play()
        if play_song:
            if event.type==pg.KEYDOWN:          
                if event.key == pg.K_q:
                    b1 = True
                    if len (lista_notas_0)>0:
                        if (lista_notas_0[0][1]>430 and lista_notas_0[0][1]<550):
                            lista_notas_0.pop(0)
                            score_player_1+=10
                        else:
                            error.play()
                        
                    else:
                        score_player_1-=3
                        error.play()
                if event.key == pg.K_w:
                    b2 = True
                    if len (lista_notas_1)>0:
                        if (lista_notas_1[0][1]>430 and lista_notas_1[0][1]<550):
                            lista_notas_1.pop(0)
                            score_player_1+=10
                        else:
                            error.play()
                        
                    else:
                        score_player_1-=3
                        error.play()
                if event.key == pg.K_e:
                    b3 = True
                    if len (lista_notas_2)>0:
                        if (lista_notas_2[0][1]>430 and lista_notas_2[0][1]<550):
                            lista_notas_2.pop(0)
                            score_player_1+=10
                        else:
                            error.play()
                    else:
                        score_player_1-=3
                        error.play()
                if event.key == pg.K_u:
                    b4 = True
                    if len (lista_notas_3)>0:
                        if (lista_notas_3[0][1]>430 and lista_notas_3[0][1]<550):
                            lista_notas_3.pop(0) 
                            score_player_2+=10
                        else:
                            error.play()
                    else:
                        score_player_2-=3
                        error.play()
                if event.key == pg.K_i:
                    b5 = True
                    if len (lista_notas_4)>0:
                        if (lista_notas_4[0][1]>430 and lista_notas_4[0][1]<550):
                            lista_notas_4.pop(0) 
                            score_player_2+=10
                        else:
                            error.play()
                    else:
                        score_player_2-=3
                        error.play()
                if event.key == pg.K_o:
                    b6 = True
                    if len (lista_notas_5)>0:
                        if (lista_notas_5[0][1]>430 and lista_notas_5[0][1]<550):
                            lista_notas_5.pop(0) 
                            score_player_2+=10
                        else:
                            error.play()
                    else:
                        score_player_2-=3
                        error.play()

            if event.type==pg.KEYUP:
                if event.key == pg.K_q:
                    b1 = False 
                if event.key == pg.K_w:
                    b2 = False 
                if event.key == pg.K_e:
                    b3 = False 
                if event.key == pg.K_u:
                    b4 = False 
                if event.key == pg.K_i:
                    b5 = False 
                if event.key == pg.K_o:
                    b6 = False 

            if event.type==time_Music:
                numero=music_time()-centecimas
                if nota != "":
                    dibujo_nota= nota.split(';')
                    if int(dibujo_nota[0])-20<= int(numero):

                        if dibujo_nota[1] =="0\n":
                            lista_notas_0.append([posicion1[0],0])
                            lista_notas_3.append([posicion4[0],0])
                        
                        if dibujo_nota[1] =="1\n":
                            lista_notas_1.append([posicion2[0],0]) 
                            lista_notas_4.append([posicion5[0],0])
                        
                        if dibujo_nota[1] =="2\n":
                            lista_notas_2.append([posicion3[0],0])
                            lista_notas_5.append([posicion6[0],0])
                            
                            
                        
                        nota=Partitura.readline()    
                    # print(nota)
                #print(int(dibujo_nota[0]))
               

aterior= 0

while True:
    events()

    screen.fill("White")
    if play_song:
        
        screen.blit(fondo,posicion)
        screen.blit(boton1,posicion1)
        screen.blit(boton2,posicion2)
        screen.blit(boton3,posicion3)
        #player 2
        screen.blit(boton4,posicion4)
        screen.blit(boton5,posicion5)
        screen.blit(boton6,posicion6)
        if b1:
            screen.blit(boton1_p,posicion1)
        if b2:
            screen.blit(boton2_p,posicion2)
        if b3:
            screen.blit(boton3_p,posicion3)
        if b4:
            screen.blit(boton4_p,posicion4)
        if b5:
            screen.blit(boton5_p,posicion5)
        if b6:
            screen.blit(boton6_p,posicion6)

        if len (lista_notas_0)>0:
            for i in range(len(lista_notas_0)):
                screen.blit(nota1,lista_notas_0[i])
                lista_notas_0[i][1]+=5

        if len (lista_notas_1)>0:
            for i in range(len(lista_notas_1)):
                screen.blit(nota2,lista_notas_1[i])
                lista_notas_1[i][1]+=5

        if len (lista_notas_2)>0:
            for i in range(len(lista_notas_2)):
                screen.blit(nota3,lista_notas_2[i])
                lista_notas_2[i][1]+=5

        if len (lista_notas_3)>0:
            for i in range(len(lista_notas_3)):
                screen.blit(nota4,lista_notas_3[i])
                lista_notas_3[i][1]+=5
        
        if len (lista_notas_4)>0:
            for i in range(len(lista_notas_4)):
                screen.blit(nota5,lista_notas_4[i])
                lista_notas_4[i][1]+=5
        
        if len (lista_notas_5)>0:
            for i in range(len(lista_notas_5)):
                screen.blit(nota6,lista_notas_5[i])
                lista_notas_5[i][1]+=5

        music_time()
        text_score1=tex_font.render(str(score_player_1),True,'White')
        text_score2=tex_font.render(str(score_player_2),True,'White')
        screen.blit(barra_de_puntaje,(0,0))
        screen.blit(text_score1,(180,30))
        screen.blit(text_score2,(605,30))
        pg.display.update()

    
        if len(lista_notas_0) !=0:
            if lista_notas_0[0][1]>555:
                lista_notas_0.pop(0)
                error.play()
        
        if len(lista_notas_1) !=0:
            if lista_notas_1[0][1]>555:
                lista_notas_1.pop(0)
                error.play()
        
        if len(lista_notas_2) !=0:
            if lista_notas_2[0][1]>555:
                lista_notas_2.pop(0)
                error.play()
        
        if len(lista_notas_3) !=0:
            if lista_notas_3[0][1]>555:
                lista_notas_3.pop(0)
                error.play()
        
        if len(lista_notas_4) !=0:
            if lista_notas_4[0][1]>555:
                lista_notas_4.pop(0)
                error.play()

        if len(lista_notas_5) !=0:
            if lista_notas_5[0][1]>555:
                lista_notas_5.pop(0)
                error.play()
        
        
        play_song=(pg.mixer.music.get_busy())
        if not play_song:
            credito_v = True

    else:

        #dibujo menu 
        pg.draw.rect(screen,'#1B9C00',(448,55, 310, 43))
        if cambio<60:
            cambio+=1
            aterior= numero_cancion - 1
            if aterior< 0:
                aterior = len(canciones)-1
            

            
        if cambio>60:
            cambio-=1
            
            aterior= numero_cancion + 1
            if aterior>= len(canciones):
                aterior = 0

        pg.draw.rect(screen,'#67445E',(456,-60+cambio, 295, 30),0,3)
        texto_cancion=tex_font2.render(canciones[aterior],True,'Black')
        screen.blit(texto_cancion,[457,-60+cambio])
            
        pg.draw.rect(screen,'#67445E',(456,cambio, 295, 30),0,3)
        texto_cancion=tex_font2.render(canciones[numero_cancion],True,'Black')
        screen.blit(texto_cancion,[457,cambio])

        pg.draw.rect(screen,'#67445E',(456,60+cambio, 295, 30),0,3)
        texto_cancion=tex_font2.render(canciones[aterior],True,'Black')
        screen.blit(texto_cancion,[457,60+cambio])

        
        screen.blit(fondo_menu,(0,0))
        screen.blit(fuego[int(anime_fuego)],(-5,400))
        screen.blit(fuego[int(anime_fuego)],(600,400))
        anime_fuego+=0.6

        if anime_fuego >= len(fuego):
            anime_fuego=0
        
        if not pg.mixer.music.get_busy():
            posicion_cancion +=1 
            numero_cancion +=1
            cambio=0
            if numero_cancion>= len(canciones):
                numero_cancion=0
            pg.mixer.music.stop()
            pg.mixer.music.load(f"./audios/{canciones[numero_cancion]}.mp3")
            pg.mixer.music.play()

        #Creditos:
        if credito_v:
            screen.blit(fondo_credito,(0,0))
            anime_credito-=0.009
            for i in range(len(tex_credito)):
                screen.blit(tex_credito[i],po_credito[i])
                po_credito[i].top+=int(anime_credito)
            if po_credito[len(po_credito)-1].bottom<-50:
                for h in range(len(tex_credito)):
                    print(50*h)
                    po_credito[h].midtop=(400,600+(50*h))
                credito_v = False

        pg.display.update()


        
        

        
            
    clock.tick(60)
    # print (lista_notas_0)
import pygame
import sys
import os

pygame.init()

directorio_actual = os.path.dirname(os.path.abspath(__file__)) #Se obtiene la ruta del directorio actual donde se encuentra el script
directorio_modulos = os.path.join(directorio_actual, '..', 'Módulos') #Se concatena la ruta del directorio actual con la carpeta que contiene el módulo
sys.path.append(directorio_modulos) #Se añade la ruta de la carpeta de módulos al sistema de rutas

import Escape_Island as EI

#Cargamos las hojas de sprites del personaje 1
quieto = pygame.image.load("Imagenes\Sprites\Personaje_1\Quieto.png")
correr = pygame.image.load("Imagenes\Sprites\Personaje_1\Correr.png")
caminar = pygame.image.load("Imagenes\Sprites\Personaje_1\Caminar.png")
ataque_1 = pygame.image.load("Imagenes\Sprites\Personaje_1\Ataque 1.png")
ataque_2 = pygame.image.load("Imagenes\Sprites\Personaje_1\Ataque 2.png")
ataque_3 = pygame.image.load("Imagenes\Sprites\Personaje_1\Ataque 3.png")
saltar = pygame.image.load("Imagenes\Sprites\Personaje_1\Salto.png")
muerte = pygame.image.load("Imagenes\Sprites\Personaje_1\Muerte.png")
defensa = pygame.image.load("Imagenes\Sprites\Personaje_1\Defensa.png")

def cargar_sprites(hoja_sprites, ancho_sprite, alto_sprite, espacio_entre_sprites):
    """Esta función toma como argumento la hoja de sprites, el ancho de cada sprite, el alto de cada sprite, el espacio entre sprites y retorna cada sprite saparado individualmente en una lista"""
    sprites = []
    for x in range(0, hoja_sprites.get_width(), espacio_entre_sprites): #Se itera entre 0 y el ancho total de la hoja de sprites con un paso de espacio_entre_sprites
        #Se extrae un sprite individiual de la hoja de sprites y se almacena en sprites
        cuadro = hoja_sprites.subsurface((x, 0, ancho_sprite, alto_sprite)) 
        sprites.append(cuadro)
    return sprites

#Extraemos los sprites individuales del personaje 1
sprites_correr = cargar_sprites(correr, correr.get_width()//8, 78, 128)
sprites_caminar = cargar_sprites(caminar, caminar.get_width()//8, 84, 128)
sprites_saltar = cargar_sprites(saltar, saltar.get_width()//10, 87, 128)

mapa_avion_ajustado =  pygame.transform.scale(EI.mapa_avion, (EI.ancho, EI.alto)) #Ajustamos el mapa al tamaño de la pantalla
EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Mostramos el mapa

altura = EI.alto * 0.3
velocidad_personaje1 = EI.ancho * 0.6
estado_caminar = None
estado_correr = None
saltando = None


while True:

    EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla

    for evento in pygame.event.get():
        if evento.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            #Si se presiona la tecla "Esc", entonces se sale de la pantalla completa
            if evento.key == pygame.K_ESCAPE:
                EI.PANTALLA = pygame.display.set_mode((500, 400))
                portada_ajustada = pygame.transform.scale(EI.portada, (500, 400))
                EI.PANTALLA.blit(portada_ajustada, (0, 0)) #Mostramos portada
            #Si se presiona la tecla "espacio", entonces el personaje salta
            if evento.key == pygame.K_SPACE:
                saltando = True
                

    if saltando:
        for sprite in sprites_saltar:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            velocidad_personaje1 += EI.ancho * 0.003
            EI.PANTALLA.blit(sprite, (velocidad_personaje1 - EI.ancho * 0.014, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
            pygame.display.flip()  #Se actualiza la pantalla
            pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
        saltando = False

    

    teclas = pygame.key.get_pressed() 
    #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
    if teclas[pygame.K_RIGHT] == False:
        EI.PANTALLA.blit(quieto, (velocidad_personaje1 + EI.ancho * 0.02, altura))


    #Si la tecla derecha está siendo presionada, entonces el personaje camina hacia la derecha
    if teclas[pygame.K_RIGHT] and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]) == False:
        velocidad_personaje1 += EI.ancho * 0.001
        if estado_caminar == None or estado_caminar == 7:
            EI.PANTALLA.blit(sprites_caminar[0], (velocidad_personaje1, altura))
            estado_caminar = 0
        elif estado_caminar == 0:
            EI.PANTALLA.blit(sprites_caminar[1], (velocidad_personaje1, altura))
            estado_caminar = 1
        elif estado_caminar == 1:
            EI.PANTALLA.blit(sprites_caminar[2], (velocidad_personaje1, altura))
            estado_caminar = 2
        elif estado_caminar == 2:
            EI.PANTALLA.blit(sprites_caminar[3], (velocidad_personaje1, altura))
            estado_caminar = 3
        elif estado_caminar == 3:
            EI.PANTALLA.blit(sprites_caminar[4], (velocidad_personaje1, altura))
            estado_caminar = 4
        elif estado_caminar == 4:
            EI.PANTALLA.blit(sprites_caminar[5], (velocidad_personaje1, altura))
            estado_caminar = 5
        elif estado_caminar == 5:
            EI.PANTALLA.blit(sprites_caminar[6], (velocidad_personaje1, altura))
            estado_caminar = 6
        elif estado_caminar == 6:
            EI.PANTALLA.blit(sprites_caminar[7], (velocidad_personaje1, altura))
            estado_caminar = 7

    #Si la tecla derecha y shift están siendo presionadas, entonces el personaje corre hacia la derecha
    if teclas[pygame.K_RIGHT] and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
        velocidad_personaje1 += EI.ancho * 0.003
        if estado_correr == None or estado_correr == 7:
            EI.PANTALLA.blit(sprites_correr[0], (velocidad_personaje1, altura))
            estado_correr = 0
        elif estado_correr == 0:
            EI.PANTALLA.blit(sprites_correr[1], (velocidad_personaje1, altura))
            estado_correr = 1
        elif estado_correr == 1:
            EI.PANTALLA.blit(sprites_correr[2], (velocidad_personaje1, altura))
            estado_correr = 2
        elif estado_correr == 2:
            EI.PANTALLA.blit(sprites_correr[3], (velocidad_personaje1, altura))
            estado_correr = 3
        elif estado_correr == 3:
            EI.PANTALLA.blit(sprites_correr[4], (velocidad_personaje1, altura))
            estado_correr = 4
        elif estado_correr == 4:
            EI.PANTALLA.blit(sprites_correr[5], (velocidad_personaje1, altura))
            estado_correr = 5
        elif estado_correr == 5:
            EI.PANTALLA.blit(sprites_correr[6], (velocidad_personaje1, altura))
            estado_correr = 6
        elif estado_correr == 6:
            EI.PANTALLA.blit(sprites_correr[7], (velocidad_personaje1, altura))
            estado_correr = 7
     

    pygame.time.Clock().tick(60) #Limitamos la cantidad de fotogramas
    
    pygame.display.update()
    
import pygame
import sys

pygame.init()

from Módulos import Escape_Island as EI

#Cargamos las hojas de sprites del personaje 1
quieto_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\quieto_derecha.png")
quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
quieto_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\quieto_izquierda.png")
quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
correr_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\correr_derecha.png")
caminar_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\caminar_derecha.png")
caminar_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\caminar_izquierda.png")
correr_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\correr_izquierda.png")
ataque1_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\\ataque1_derecha.png")
ataque1_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\\ataque1_izquierda.png")
ataque3_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\\ataque3_derecha.png")
ataque3_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\\ataque3_izquierda.png")
saltar_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\saltar_derecha.png")
saltar_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\saltar_izquierda.png")
muerte = pygame.image.load("Imagenes\Sprites\Personaje_1\Muerte.png")
defensa = pygame.image.load("Imagenes\Sprites\Personaje_1\Defensa.png")

def cargar_sprites(hoja_sprites, ancho_sprite, alto_sprite, espacio_entre_sprites):
    """Esta función toma como argumento la hoja de sprites, el ancho de cada sprite, el alto de cada sprite, el espacio entre sprites y retorna cada sprite saparado individualmente en una lista"""
    sprites = []
    for x in range(0, hoja_sprites.get_width(), espacio_entre_sprites): #Se itera entre 0 y el ancho total de la hoja de sprites con un paso de espacio_entre_sprites
        #Se extrae un sprite individiual de la hoja de sprites y se almacena en sprites
        cuadro = hoja_sprites.subsurface((x, 0, ancho_sprite, alto_sprite)) 
        cuadro = pygame.transform.scale(cuadro, (EI.ancho * 0.09, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
        sprites.append(cuadro)
    return sprites

#Extraemos los sprites individuales del personaje 1
sprites_correr_derecha = cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 78, 128)
sprites_caminar_derecha = cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 84, 128)
sprites_saltar_derecha = cargar_sprites(saltar_derecha, saltar_derecha.get_width()//10, 87, 128)
sprites_saltar_izquierda = cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//10, 87, 128)
sprites_caminar_izquierda = cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 84, 128)
sprites_correr_izquierda = cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 78, 128)
sprites_ataque3_derecha = cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 81, 128)
sprites_ataque3_izquierda = cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 81, 128)
sprites_ataque1_derecha = cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//4, 84, 128)
sprites_ataque1_izquierda = cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//4, 84, 128)

mapa_avion_ajustado =  pygame.transform.scale(EI.mapa_avion, (EI.ancho, EI.alto)) #Ajustamos el mapa al tamaño de la pantalla
EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Mostramos el mapa

altura = EI.alto * 0.3
velocidad_personaje1 = EI.ancho * 0.6
estado_caminar_derecha = None
estado_caminar_izquierda = None
estado_correr_derecha = None
estado_correr_izquierda = None
saltando = None
anterior = None
ataque1 = None
ataque3 = None
fullscreen = True

while True:

    EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla

    for evento in pygame.event.get():
        if evento.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            #Si se presiona la tecla "Esc", entonces se sale de la pantalla completa
            if evento.key == pygame.K_ESCAPE and fullscreen:
                fullscreen = False
                pygame.quit()
                pygame.init()
                EI.PANTALLA = pygame.display.set_mode((EI.ancho - (EI.ancho * 0.1), EI.alto - (EI.alto * 0.2)))
                portada_ajustada = pygame.transform.scale(EI.portada,(EI.ancho - (EI.ancho * 0.1), EI.alto - (EI.alto * 0.2)))
                EI.PANTALLA.blit(portada_ajustada, (0, 0)) #Mostramos portada
                mapa_avion_ajustado =  pygame.transform.scale(EI.mapa_avion, (EI.ancho - (EI.ancho * 0.1), EI.alto - (EI.alto * 0.2)))
                altura -= EI.alto * 0.076
                velocidad_personaje1 -= EI.ancho * 0.06
            #Si se presiona la tecla "f", entoces vuelve a pantalla completa
            if evento.key == pygame.K_f and not fullscreen:
                fullscreen = True
                pygame.quit()
                pygame.init()
                EI.PANTALLA = pygame.display.set_mode((EI.ancho, EI.alto))
                portada_ajustada = pygame.transform.scale(EI.portada, (EI.ancho, EI.alto))
                EI.PANTALLA.blit(portada_ajustada, (0, 0)) #Mostramos portada
                mapa_avion_ajustado =  pygame.transform.scale(EI.mapa_avion, (EI.ancho, EI.alto))
                altura += EI.alto * 0.076
                velocidad_personaje1 += EI.ancho * 0.06
            #Si se presiona la tecla "espacio", entonces el personaje salta
            if evento.key == pygame.K_SPACE:
                saltando = True
            #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1
            if evento.key == pygame.K_x:
                ataque1 = True
            #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3
            if evento.key == pygame.K_z:
                ataque3 = True

    #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
    if ataque1 and (anterior == "derecha" or anterior == None):
        for sprite in sprites_ataque1_derecha:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            velocidad_personaje1 += EI.ancho * 0.003
            EI.PANTALLA.blit(sprite, (velocidad_personaje1 - EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
            pygame.display.flip()  #Se actualiza la pantalla
            pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
        ataque1 = False

    #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
    if ataque1 and (anterior == "izquierda"):
        for sprite in sprites_ataque1_izquierda[::-1]:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            velocidad_personaje1 -= EI.ancho * 0.003
            EI.PANTALLA.blit(sprite, (velocidad_personaje1 + EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
            pygame.display.flip()  #Se actualiza la pantalla
            pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
        ataque1 = False

    #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
    if ataque3 and (anterior == "derecha" or anterior == None):
        for sprite in sprites_ataque3_derecha:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            velocidad_personaje1 += EI.ancho * 0.003
            EI.PANTALLA.blit(sprite, (velocidad_personaje1 - EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
            pygame.display.flip()  #Se actualiza la pantalla
            pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
        ataque3 = False

    #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
    if ataque3 and (anterior == "izquierda"):
        for sprite in sprites_ataque3_izquierda[::-1]:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            velocidad_personaje1 -= EI.ancho * 0.003
            EI.PANTALLA.blit(sprite, (velocidad_personaje1 + EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
            pygame.display.flip()  #Se actualiza la pantalla
            pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
        ataque3 = False

    #Si se presiona la tecla "espacio", entonces el personaje salta
    if saltando and (anterior == "derecha" or anterior == None):
        for sprite in sprites_saltar_derecha:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            velocidad_personaje1 += EI.ancho * 0.003
            EI.PANTALLA.blit(sprite, (velocidad_personaje1 - EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
            pygame.display.flip()  #Se actualiza la pantalla
            pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
        saltando = False

    #Si se presiona la tecla "espacio", entonces el personaje salta
    if saltando and (anterior == "izquierda"):
        for sprite in sprites_saltar_izquierda[::-1]:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            velocidad_personaje1 -= EI.ancho * 0.003
            EI.PANTALLA.blit(sprite, (velocidad_personaje1 + EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
            pygame.display.flip()  #Se actualiza la pantalla
            pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
        saltando = False

    teclas = pygame.key.get_pressed() 

    #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
    if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
        EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje1 + EI.ancho * 0.027, altura))
    if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
        EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje1 + EI.ancho * 0.04, altura))

    #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
    if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "derecha" or anterior == None):
        altura += EI.alto * 0.01
        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje1 + EI.ancho * 0.027, altura))

    #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
    if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "izquierda"):
        altura += EI.alto * 0.01
        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje1 + EI.ancho * 0.04, altura))
    
    #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
    if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "derecha" or anterior == None):
        altura -= EI.alto * 0.01
        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje1 + EI.ancho * 0.027, altura))
    
    #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
    if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "izquierda"):
        altura -= EI.alto * 0.01
        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje1 + EI.ancho * 0.04, altura))

    #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
    if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]) == False:
        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        velocidad_personaje1 += EI.ancho * 0.002 
        anterior = "derecha"
        if estado_caminar_derecha == None or estado_caminar_derecha == 7:
            EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje1, altura))
            estado_caminar_derecha = 0
        elif estado_caminar_derecha == 0:
            EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje1, altura))
            estado_caminar_derecha = 1
        elif estado_caminar_derecha == 1:
            EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje1, altura))
            estado_caminar_derecha = 2
        elif estado_caminar_derecha == 2:
            EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje1, altura))
            estado_caminar_derecha = 3
        elif estado_caminar_derecha == 3:
            EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje1, altura))
            estado_caminar_derecha = 4
        elif estado_caminar_derecha == 4:
            EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje1, altura))
            estado_caminar_derecha = 5
        elif estado_caminar_derecha == 5:
            EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje1, altura))
            estado_caminar_derecha = 6
        elif estado_caminar_derecha == 6:
            EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje1, altura))
            estado_caminar_derecha = 7

    #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
    if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]) == False:
        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        velocidad_personaje1 -= EI.ancho * 0.002 
        anterior = "izquierda"
        if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
            EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje1, altura))
            estado_caminar_izquierda = 0
        elif estado_caminar_izquierda == 0:
            EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje1, altura))
            estado_caminar_izquierda = 1
        elif estado_caminar_izquierda == 1:
            EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje1, altura))
            estado_caminar_izquierda = 2
        elif estado_caminar_izquierda == 2:
            EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje1, altura))
            estado_caminar_izquierda = 3
        elif estado_caminar_izquierda == 3:
            EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje1, altura))
            estado_caminar_izquierda = 4
        elif estado_caminar_izquierda == 4:
            EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje1, altura))
            estado_caminar_izquierda = 5
        elif estado_caminar_izquierda == 5:
            EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje1, altura))
            estado_caminar_izquierda = 6
        elif estado_caminar_izquierda == 6:
            EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje1, altura))
            estado_caminar_izquierda = 7

    #Si la tecla derecha o "d" y shift están siendo presionadas, entonces el personaje corre hacia la derecha
    if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
        velocidad_personaje1 += EI.ancho * 0.003
        anterior = "derecha"
        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        if estado_correr_derecha == None or estado_correr_derecha == 7:
            EI.PANTALLA.blit(sprites_correr_derecha[0], (velocidad_personaje1, altura))
            estado_correr_derecha = 0
        elif estado_correr_derecha == 0:
            EI.PANTALLA.blit(sprites_correr_derecha[1], (velocidad_personaje1, altura))
            estado_correr_derecha = 1
        elif estado_correr_derecha == 1:
            EI.PANTALLA.blit(sprites_correr_derecha[2], (velocidad_personaje1, altura))
            estado_correr_derecha = 2
        elif estado_correr_derecha == 2:
            EI.PANTALLA.blit(sprites_correr_derecha[3], (velocidad_personaje1, altura))
            estado_correr_derecha = 3
        elif estado_correr_derecha == 3:
            EI.PANTALLA.blit(sprites_correr_derecha[4], (velocidad_personaje1, altura))
            estado_correr_derecha = 4
        elif estado_correr_derecha == 4:
            EI.PANTALLA.blit(sprites_correr_derecha[5], (velocidad_personaje1, altura))
            estado_correr_derecha = 5
        elif estado_correr_derecha == 5:
            EI.PANTALLA.blit(sprites_correr_derecha[6], (velocidad_personaje1, altura))
            estado_correr_derecha = 6
        elif estado_correr_derecha == 6:
            EI.PANTALLA.blit(sprites_correr_derecha[7], (velocidad_personaje1, altura))
            estado_correr_derecha = 7

    #Si la tecla izquierda o "a" y shift están siendo presionadas, entonces el personaje corre hacia la izquierda
    if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
        velocidad_personaje1 -= EI.ancho * 0.003
        anterior = "izquierda"
        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        if estado_correr_izquierda == None or estado_correr_izquierda == 7:
            EI.PANTALLA.blit(sprites_correr_izquierda[7], (velocidad_personaje1, altura))
            estado_correr_izquierda = 0
        elif estado_correr_izquierda == 0:
            EI.PANTALLA.blit(sprites_correr_izquierda[6], (velocidad_personaje1, altura))
            estado_correr_izquierda = 1
        elif estado_correr_izquierda == 1:
            EI.PANTALLA.blit(sprites_correr_izquierda[5], (velocidad_personaje1, altura))
            estado_correr_izquierda = 2
        elif estado_correr_izquierda == 2:
            EI.PANTALLA.blit(sprites_correr_izquierda[4], (velocidad_personaje1, altura))
            estado_correr_izquierda = 3
        elif estado_correr_izquierda == 3:
            EI.PANTALLA.blit(sprites_correr_izquierda[3], (velocidad_personaje1, altura))
            estado_correr_izquierda = 4
        elif estado_correr_izquierda == 4:
            EI.PANTALLA.blit(sprites_correr_izquierda[2], (velocidad_personaje1, altura))
            estado_correr_izquierda = 5
        elif estado_correr_izquierda == 5:
            EI.PANTALLA.blit(sprites_correr_izquierda[1], (velocidad_personaje1, altura))
            estado_correr_izquierda = 6
        elif estado_correr_izquierda == 6:
            EI.PANTALLA.blit(sprites_correr_izquierda[0], (velocidad_personaje1, altura))
            estado_correr_izquierda = 7

    pygame.time.Clock().tick(60) #Limitamos la cantidad de fotogramas
    
    pygame.display.update()
    

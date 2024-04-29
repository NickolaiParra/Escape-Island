import pygame
import sys

pygame.init()

from Módulos import Escape_Island as EI

#Texto
fuente_2 = pygame.font.Font("Fuentes\\Nicolast.otf", int(EI.ancho * 0.04)) 
texto_seleccionar = fuente_2.render('Selecciona   tu   personaje', True, (EI.ROJO))

#Botones
boton_personaje1 = EI.Boton(EI.ancho * 0.1, EI.alto * 0.27, EI.ancho * 0.2, EI.alto * 0.5, "", 0, 0)
boton_personaje2 = EI.Boton(EI.ancho * 0.4, EI.alto * 0.27, EI.ancho * 0.2, EI.alto * 0.5, "", 0, 0)
boton_personaje3 = EI.Boton(EI.ancho * 0.7, EI.alto * 0.27, EI.ancho * 0.2, EI.alto * 0.5, "", 0, 0)
boton_cancelar = EI.Boton(EI.ancho * 0.2, EI.alto * 0.85, EI.ancho * 0.2, EI.alto * 0.1, "Cancelar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))
boton_aceptar = EI.Boton(EI.ancho * 0.6, EI.alto * 0.85, EI.ancho * 0.2, EI.alto * 0.1, "Aceptar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))

#Imágenes
#Personaje 1
quieto_derecha1 = pygame.image.load("Imagenes\Sprites\Personaje_1\quieto_derecha.png")
quieto_derecha1 = pygame.transform.scale(quieto_derecha1, (EI.ancho * 0.09, EI.alto * 0.4)) #Se adecua el sprite a un tamaño específico
#Personaje 2
quieto_derecha2 = pygame.image.load("Imagenes\Sprites\Personaje_2\quieto_derecha.png")
quieto_derecha2 = pygame.transform.scale(quieto_derecha2, (EI.ancho * 0.1, EI.alto * 0.4)) #Se adecua el sprite a un tamaño específico
#Personaje 3
quieto_derecha3 = pygame.image.load("Imagenes\Sprites\Personaje_3\quieto_derecha.png")
quieto_derecha3 = pygame.transform.scale(quieto_derecha3, (EI.ancho * 0.19, EI.alto * 0.34)) #Se adecua el sprite a un tamaño específico
#Candado
candado_cerrado = pygame.image.load("Imagenes\Iconos\Candado_cerrado.png")
candado_cerrado = pygame.transform.scale(candado_cerrado, (EI.ancho * 0.15, EI.alto * 0.3)) #Se adecua la imagen a un tamaño específico
candado_abierto = pygame.image.load("Imagenes\Iconos\Candado_abierto.png")

p1 = False
p2 = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            #Si se presiona la tecla "Esc", entonces se sale del juego
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        #Si se da click con el mouse encima de algún botón, entonces su color cambia
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_personaje1.esta_encima(evento.pos):
            boton_personaje1.color_normal = EI.ROJO 
            boton_personaje2.color_normal = EI.AZUL
            boton_personaje3.color_normal = EI.AZUL
            p1 = True
            p2 = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_personaje2.esta_encima(evento.pos):
            boton_personaje2.color_normal = EI.ROJO
            boton_personaje1.color_normal = EI.AZUL 
            boton_personaje3.color_normal = EI.AZUL
            p2 = True
            p1 = False

        if evento.type == pygame.MOUSEMOTION:
            #Si el cursor del mouse pasa por encima de algún  botón, entonces su color cambia
            boton_personaje1.color_normal = EI.AZUL if not boton_personaje1.esta_encima(evento.pos) and not p1 else EI.ROJO
            boton_personaje2.color_normal = EI.AZUL if not boton_personaje2.esta_encima(evento.pos) and not p2 else EI.ROJO
            boton_personaje3.color_normal = EI.AZUL if not boton_personaje3.esta_encima(evento.pos) else EI.GRIS
            boton_aceptar.color_normal = EI.AZUL if not boton_aceptar.esta_encima(evento.pos) else EI.ROJO
            boton_cancelar.color_normal = EI.AZUL if not boton_cancelar.esta_encima(evento.pos) else EI.ROJO
        
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_aceptar.esta_encima(evento.pos):
            seleccion = 1 if p1 else 2

        


    EI.PANTALLA.fill(EI.FONDO) #Se limpia la pantalla
    #Mostramos los botones
    boton_personaje1.dibujar(EI.PANTALLA)
    boton_personaje2.dibujar(EI.PANTALLA)
    boton_personaje3.dibujar(EI.PANTALLA)
    boton_cancelar.dibujar(EI.PANTALLA)
    boton_aceptar.dibujar(EI.PANTALLA)
    
    EI.PANTALLA.blit(quieto_derecha1, (EI.ancho * 0.15, EI.alto * 0.32)) #Se imprime la imágen del personaje 1
    EI.PANTALLA.blit(quieto_derecha2, (EI.ancho * 0.45, EI.alto * 0.32)) #Se imprime la imágen del personaje 2
    EI.PANTALLA.blit(quieto_derecha3, (EI.ancho * 0.705, EI.alto * 0.37)) #Se imprime la imágen del personaje 3
    EI.PANTALLA.blit(candado_cerrado, (EI.ancho * 0.725, EI.alto * 0.35)) #Se imprime la imágen del candado cerrado

    EI.PANTALLA.blit(texto_seleccionar, (EI.ancho * 0.2, EI.alto * 0.1)) #Se imprime el texto "Selecciona tu personaje"
    

    pygame.display.flip() #Actualizar la pantalla
            
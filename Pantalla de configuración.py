import pygame
import sys
from Módulos import Escape_Island as EI

#Inicializamos pygame
pygame.init()

#Inicializamos el módulo de sonido de pygame
pygame.mixer.init()


#Configuración de la música
pygame.mixer.music.load('Música\ST.mp3') #Cargamos la música
pygame.mixer.music.set_volume(0.5)  #Configuramos el volumen inicial
pygame.mixer.music.play(-1)  #Reproducimos la música en bucle 

#Textos
fuente_2 = pygame.font.Font("Fuentes\\Nicolast.otf", int(EI.ancho * 0.04)) #Fuente del texto de la pantalla de inicio
texto_musica = fuente_2.render('Music', True, (EI.ROJO)) 

#Botones
boton_cancelar = EI.Boton(EI.ancho * 0.1, EI.alto * 0.8, EI.ancho * 0.2, EI.alto * 0.1, "Cancelar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))
boton_aceptar = EI.Boton(EI.ancho * 0.5, EI.alto * 0.8, EI.ancho * 0.2, EI.alto * 0.1, "Aceptar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))

iconosonido_ajustado = pygame.transform.scale(EI.icono_sonido, (EI.ancho * 0.07, EI.alto * 0.1)) 
iconosinsonido_ajustado = pygame.transform.scale(EI.icono_sinsonido, (EI.ancho * 0.07, EI.alto * 0.1)) 

posicion_relativa = 0.5
mouseantiguo_x = EI.ancho * 0.34
Gris = True

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEMOTION:
            #Si el cursor del mouse pasa por encima de algún  botón, entonces su color cambia
            boton_aceptar.color_normal = EI.AZUL if not boton_aceptar.esta_encima(evento.pos) else EI.ROJO
            boton_cancelar.color_normal = EI.AZUL if not boton_cancelar.esta_encima(evento.pos) else EI.ROJO
        
    EI.PANTALLA.fill(EI.FONDO) #Se limpia la pantalla
    if posicion_relativa != 0:
        EI.PANTALLA.blit(iconosonido_ajustado, (EI.ancho * 0.07, EI.alto * 0.07)) #Se imprime el icono del sonido
        Gris = True
    else: 
        EI.PANTALLA.blit(iconosinsonido_ajustado, (EI.ancho * 0.07, EI.alto * 0.069)) #Se imprime el icono de que no hay sonido
        Gris = False

    EI.PANTALLA.blit(texto_musica, (EI.ancho * 0.55, EI.alto * 0.085)) #Se imprime el texto "Music"

    mouse_x, mouse_y = pygame.mouse.get_pos() #Obtenemos la posición del mouse

    if EI.alto * 0.09 <= mouse_y <= EI.alto * 0.09 + EI.alto * 0.05 and EI.ancho * 0.195 <= mouse_x <= EI.ancho * 0.489:  #Verificamos si el mouse está dentro de los límites de la barra 
        posicion_relativa = (mouse_x - (EI.ancho * 0.2)) / (EI.ancho * 0.3) #Calculamos la posición relativa del control deslizante azul en la barra 
        posicion_relativa = max(0, min(1, posicion_relativa)) #Asegurarse de que la posición relativa esté en el rango [0, 1]
        volumen = posicion_relativa

        pygame.mixer.music.set_volume(volumen) #Establecer volumen de la música
        if Gris:
            EI.dibujar_barra(mouse_x, EI.NEGRO, EI.AZUL, EI.AZUL) #Dibujar barra desplazable
        else: EI.dibujar_barra(mouse_x, EI.GRIS, EI.AZUL, EI.GRIS) #Dibujar barra desplazable
        mouseantiguo_x = mouse_x
    else:
        if Gris:
            EI.dibujar_barra(mouseantiguo_x, EI.NEGRO, EI.AZUL, EI.AZUL) #Dibujar barra desplazable
        else: EI.dibujar_barra(mouseantiguo_x, EI.GRIS, EI.AZUL, EI.GRIS) #Dibujar barra desplazable

    #Mostramos los botones
    boton_cancelar.dibujar(EI.PANTALLA)
    boton_aceptar.dibujar(EI.PANTALLA)

    pygame.display.flip() #Actualizar la pantalla

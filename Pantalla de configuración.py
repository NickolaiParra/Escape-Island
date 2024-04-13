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

def dibujar_barra(pos_x):
    """Esta función toma como argumento la posición x del mouse y dibuja una barra con control deslizante"""
    pygame.draw.rect(EI.PANTALLA, EI.BLANCO, (EI.ancho * 0.2, EI.alto * 0.1, EI.ancho * 0.3, EI.alto * 0.03))  #Barra blanca
    pygame.draw.rect(EI.PANTALLA, EI.AZUL, (pos_x, EI.alto * 0.09, EI.ancho * 0.02, EI.alto * 0.05))  #Control deslizante azul

mouseantiguo_x = EI.ancho * 0.34

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    EI.PANTALLA.fill(EI.NEGRO) #Se limpia la pantalla
    
    mouse_x, mouse_y = pygame.mouse.get_pos() #Obtenemos la posición del mouse

    if EI.alto * 0.09 <= mouse_y <= EI.alto * 0.09 + EI.alto * 0.05 and EI.ancho * 0.195 <= mouse_x <= EI.ancho * 0.489:  #Verificamos si el mouse está dentro de los límites de la barra blanca
        posicion_relativa = (mouse_x - (EI.ancho * 0.2)) / (EI.ancho * 0.3) #Calculamos la posición relativa del control deslizante azul en la barra blanca
        posicion_relativa = max(0, min(1, posicion_relativa)) #Asegurarse de que la posición relativa esté en el rango [0, 1]
        volumen = posicion_relativa

        pygame.mixer.music.set_volume(volumen) #Establecer volumen de la música
        dibujar_barra(mouse_x) #Dibujar barra desplazable
        mouseantiguo_x = mouse_x
    else:
        dibujar_barra(mouseantiguo_x) #Dibujar barra desplazable

    pygame.display.flip() #Actualizar la pantalla

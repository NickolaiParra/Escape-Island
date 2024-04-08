import pygame
import sys
import os

directorio_actual = os.path.dirname(os.path.abspath(__file__)) #Se obtiene la ruta del directorio actual donde se encuentra el script
directorio_modulos = os.path.join(directorio_actual, '..', 'Módulos') #Se concatena la ruta del directorio actual con la carpeta que contiene el módulo
sys.path.append(directorio_modulos) #Se añade la ruta de la carpeta de módulos al sistema de rutas

import Escape_Island as EI


pygame.init()

mapa_avion_ajustado =  pygame.transform.scale(EI.mapa_avion, (EI.ancho, EI.alto)) #Ajustamos el mapa al tamaño de la pantalla
EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Mostramos el mapa
while True:
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
    pygame.display.update()
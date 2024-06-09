import pygame
import sys
from Módulos import Escape_Island as EI

#Inicialización de Pygame
pygame.init()


fuente_codigo = pygame.font.Font("Fuentes\\FiraCode.otf", int(EI.ancho * 0.02)) 
tamaño_fuente = int(EI.ancho * 0.02)
lines = [""]
cursor_pos = [0, 0]  #Posición del cursor

num_dialog = -1
dialog_continue = True

#personajes
muerte = pygame.transform.scale(EI.muerte, (EI.ancho*0.2, EI.alto*0.3))
muerte_rect = muerte.get_rect()
muerte_rect.bottomleft = (EI.ancho*0.01, EI.alto*0.7)

#Imágenes
fondo_guerra = pygame.transform.scale(EI.fondo_guerra, (EI.ancho, EI.alto))

# Bucle principal del juego
while True:
    if num_dialog == -1:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        t1 = "Este lugar está en ruinas."
        t2 = "Pero es la única manera de escapar."
        EI.mostrar_texto("Examen final",t1,t2,color=EI.ROJO)
    elif num_dialog == 0:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Es increíble que hayas podido llegar hasta aquí."
        t2 = "Lamentablemente, hasta acá llegó tu aventura."
        EI.mostrar_texto("Muerte",t1,t2,color=EI.MORADO)
    elif num_dialog == 1:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "La única manera de salir con vida es superando el siguiente desafío."
        t2 = "Esta vez, no será de opción múltiple."
        t3 = "Deberás escribir tu propio código."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 2:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Debes -------------------------"
        EI.mostrar_texto("Muerte",t1,t2,color=EI.MORADO)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            #Si se presiona la flecha izquierda o derecha, se avanza en los diálogos
            elif event.key == pygame.K_RIGHT and dialog_continue:
                #Avanzar el diálogo
                num_dialog += 1
            elif num_dialog >= 0 and event.key == pygame.K_LEFT and dialog_continue:
                #Retroceder el diálogo
                num_dialog -= 1
            elif num_dialog == 3: 
                dialog_continue = False
                EI.keydown(cursor_pos, lines, event)
                EI.mostrar_texto("Desafío final", "Presiona 'Ctrl' para ejecutar tu código.",EI.t,color=EI.ROJO)
    if num_dialog == 3:  
        dialog_continue = False    
        EI.render_text(cursor_pos, lines, fuente_codigo, tamaño_fuente)
        EI.mostrar_texto("Desafío final", "Presiona 'Ctrl' para ejecutar tu código.",EI.t,color=EI.ROJO)
    pygame.display.flip()

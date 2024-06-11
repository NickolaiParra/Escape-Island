import pygame
import sys
import time
from Módulos import Escape_Island as EI

#Inicialización de Pygame
pygame.init()

tiempo_inicio = time.time() #Tiempo de inicio del programa

fuente_codigo = pygame.font.Font("Fuentes\\FiraCode.otf", int(EI.ancho * 0.02)) 
tamaño_fuente = int(EI.ancho * 0.02)
lines = [[""]]
cursor_pos= [[0, 0]]
current_screen = 0
num_screens = 3  # Número de pantallas
for _ in range(num_screens - 1):
    lines.append([""])
for _ in range(num_screens - 1):
    cursor_pos.append([0, 0])

num_dialog = -1
dialog_continue = True

#personajes
muerte = pygame.transform.scale(EI.muerte, (EI.ancho*0.2, EI.alto*0.3))
muerte_rect = muerte.get_rect()
muerte_rect.bottomleft = (EI.ancho*0.01, EI.alto*0.7)

#Imágenes
fondo_guerra = pygame.transform.scale(EI.fondo_guerra, (EI.ancho, EI.alto))
fondo_final = pygame.transform.scale(EI.fondo_final, (EI.ancho, EI.alto))

# Bucle principal del juego
while True:
    if num_dialog == -1:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        t1 = "Este lugar está en ruinas."
        t2 = "Pero es la única manera de escapar..."
        EI.mostrar_texto("Examen final",t1,t2,color=EI.ROJO)
    elif num_dialog == 0:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Es increíble que hayas podido llegar hasta aquí."
        t2 = "Lamentablemente, hasta acá llegó tu aventura."
        t3 = "La única manera de salir con vida es superando el siguiente desafío."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 1:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Esta vez, no será de opción múltiple."
        t2 = "Deberás escribir tu propio código."
        EI.mostrar_texto("Muerte",t1,t2,color=EI.MORADO)
    elif num_dialog == 2:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Necesitas desplazarte hasta la salida para ser rescatado."
        t2 = "La isla está representada como una cuadrícula de 100 x 100."
        t3 = "Cada celda tiene coordenadas (x, y) que van desde (1, 1) hasta (100, 100)."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 3:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "La salida está ubicada en una celda aleatoria de esta cuadrícula."
        t2 = "Tu objetivo será crear la función 'escape_island'."
        t3 = "Esta función debe recibir cuatro argumentos: 'x', 'y', 'salida_x', 'salida_y'. (En ese orden)."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 4:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "La posición 'x' de la salida está representada por la variable 'salida_x'."
        t2 = "La posición 'y' de la salida está representada por la variable 'salida_y'."
        t3 = "Tú te encuentras en la posición (x, y) de la isla."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 5:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Para escapar de la isla, debes moverte paso a paso hacia la salida."
        t2 = "Solo puedes hacer movimientos horizontales y verticales."
        t3 = "Solo puedes hacer un movimiento por cada paso."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 6:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "La función debe retornar la menor cantidad de pasos necesarios para llegar hasta la salida."
        t2 = "Por ejemplo, si la entrada es (5, 4, 1, 1). La función debe retornar: 7"
        t3 = "Por ejemplo, si la entrada es (100, 100, 100, 100). La función debe retornar: 0"
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 7:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Por ejemplo, si la entrada es (2, 10, 2, 1). La función debe retornar: 9"
        t2 = "Ten cuidado con el nombre de la función."
        t3 = "Si lo logras, serás libre."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 9:
        examen_final = False
        EI.PANTALLA.blit(fondo_final, (0, 0))
        t1 = "¡Felicidades, has logrado escapar de la isla!"
        t2 = "Has demostrado gran ingenio en cada desafío."
        t3 = "¡Ahora eres libre!"
        EI.mostrar_texto("Escape Island",t1,t2,t3,color=EI.ROJO)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            #Si se presiona 'F1', 'F2' o 'F3' se cambia de pantalla
            if event.key == pygame.K_F1:
                current_screen = 0
            elif event.key == pygame.K_F2:
                current_screen = 1
            elif event.key == pygame.K_F3:
                current_screen = 2
            #Si se presiona la flecha izquierda o derecha, se avanza en los diálogos
            if event.key == pygame.K_RIGHT and dialog_continue:
                #Avanzar el diálogo
                num_dialog += 1
            elif num_dialog >= 0 and event.key == pygame.K_LEFT and dialog_continue:
                #Retroceder el diálogo
                num_dialog -= 1
            elif num_dialog == 8: 
                dialog_continue = False
                examen_final = True
                t1 = "Desafío final: Crea la función 'escape_island' (x, y, salida_x, salida_y)."
                t2 = "Debes retornar la menor cantidad de pasos para llegar a la salida."
                t3 = "Presiona 'Ctrl' para ejecutar tu código. Utiliza 'F1', 'F2' y 'F3' si necesitas escribir más código."
                EI.keydown(cursor_pos[current_screen], lines[current_screen], lines, event)
                EI.mostrar_texto(t1,t2,t3,EI.t,color=EI.ROJO)
    if num_dialog == 8:  
        t1 = "Desafío final: Crea la función 'escape_island' (x, y, salida_x, salida_y)."
        t2 = "Debes retornar la menor cantidad de pasos para llegar a la salida."
        t3 = "Presiona 'Ctrl' para ejecutar tu código. Utiliza 'F1', 'F2' y 'F3' si necesitas escribir más código."
        dialog_continue = False
        examen_final = True  
        EI.render_text(cursor_pos[current_screen], lines[current_screen], fuente_codigo, tamaño_fuente)
        EI.mostrar_texto(t1, t2, t3,EI.t,color=EI.ROJO)
        if EI.correcto:  
            pygame.time.wait(1000)
            num_dialog = 9
    pygame.display.flip()

import pygame
from Módulos import Escape_Island as EI

#Inicialización de Pygame
pygame.init()

#Definición de constantes
tamaño_fuente = int(EI.ancho * 0.02)

#Configurar la fuente
fuente_codigo = pygame.font.Font("Fuentes\\FiraCode.otf", int(EI.ancho * 0.02)) 

#Variables del editor
lines = [""]
cursor_pos = [0, 0]  #Posición del cursor

#Lista con palabras reservadas importantes
palabras_reservadas = ['if', 'while', 'for', 'True', 'False', 'def', 'print', 'and', 'or', 'elif', 'else', 'in']

def render_text(): 
    '''Esta función muestra el texto y el cursor de un editor de código'''
    EI.PANTALLA.fill(EI.NEGRO) #Se limpia la pantalla
    y = 0
    for line in lines: #Se itera en cada línea
        linea_renderizada = fuente_codigo.render(line, True, EI.BLANCO)  #Renderizar la palabra en blanco
        EI.PANTALLA.blit(linea_renderizada, (EI.ancho * 0.005, y))  #Se muestra la palabra en la pantalla
        y += tamaño_fuente + EI.alto * 0.008  #Se ajusta la posición vertical para la siguiente línea

    # Se calcula la posición del cursor
    cursor_x = EI.ancho * 0.005 + fuente_codigo.size(lines[cursor_pos[0]][:cursor_pos[1]])[0]
    cursor_y = cursor_pos[0] * tamaño_fuente + (EI.alto * 0.01) * cursor_pos[0]
    pygame.draw.line(EI.PANTALLA, EI.BLANCO, (cursor_x, cursor_y), (cursor_x, cursor_y + tamaño_fuente), int(EI.ancho * 0.0015))
    


def keydown(event):
    '''Esta función maneja los eventos en un editor de código'''
    key = event.key
    line, pos = cursor_pos 
    current_line = lines[line]
    
    if key == pygame.K_KP_ENTER or key == pygame.K_RETURN:
        if current_line.endswith(':'):
            #Si se presiona enter luego de dos puntos, se salta de línea y se pone una tabulación
            lines.insert(line + 1, "    ")
            cursor_pos[0] += 1
            cursor_pos[1] = 4
        else: #Si se presiona enter, se salta de línea
            lines.insert(line + 1, "")
            cursor_pos[0] += 1
            cursor_pos[1] = 0

    elif key == pygame.K_BACKSPACE:
        #Si se presiona la tecla 'Backspace', entonces se borra el caracter
        if pos > 0:
            lines[line] = current_line[:pos - 1] + current_line[pos:]
            cursor_pos[1] -= 1
        elif line > 0:
            cursor_pos[0] -= 1
            cursor_pos[1] = len(lines[cursor_pos[0]])
            lines[cursor_pos[0]] += lines.pop(line) #Fusiona la línea actual con la anterior

    elif key == pygame.K_TAB:
        #Si se presiona 'Tab', entonces se ponen 4 espacios
        lines[line] = current_line[:pos] + ' ' * 4 + current_line[pos:]
        cursor_pos[1] += 4

    elif key == pygame.K_LEFT:
        #Si se presiona la flecha izquierda, entonces el cursor se mueve a la izquierda
        if pos > 0:
            cursor_pos[1] -= 1
        elif line > 0:
            cursor_pos[0] -= 1
            cursor_pos[1] = len(lines[cursor_pos[0]])

    elif key == pygame.K_RIGHT:
        #Si se presiona la flecha derecha, entonces el cursor se mueve a la derecha
        if pos < len(current_line):
            cursor_pos[1] += 1
        elif line < len(lines) - 1:
            cursor_pos[0] += 1
            cursor_pos[1] = 0

    elif key == pygame.K_UP:
        #Si se presiona la flecha hacia arriba, entonces el cursor sube
        if line > 0:
            cursor_pos[0] -= 1
            cursor_pos[1] = min(cursor_pos[1], len(lines[cursor_pos[0]]))

    elif key == pygame.K_DOWN:
        #Si se presiona la flecha hacia abajo, entonces el cursor baja
        if line < len(lines) - 1:
            cursor_pos[0] += 1
            cursor_pos[1] = min(cursor_pos[1], len(lines[cursor_pos[0]]))

    elif key == pygame.K_LCTRL or key == pygame.K_RCTRL:
        #Si se presiona 'Ctrl', entonces el código se ejecuta
        code = '\n'.join(lines)
        try:
            exec(code)
        except:
            print("Error al ejecutar el código")

    else:
        #Se agrega el caracter
        char = event.unicode
        lines[line] = current_line[:pos] + char + current_line[pos:]
        cursor_pos[1] += 1


# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            else: keydown(event)
    print(cursor_pos)
    render_text()
    pygame.display.flip()

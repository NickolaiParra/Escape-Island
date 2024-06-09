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
 

def render_text():
    '''Esta función muestra el texto y el cursor de un editor de código'''
    # Lista con palabras reservadas importantes
    palabras_reservadas = ['True', 'False', 'print']
    palabras_reservadas_condicionales = ['if', 'and', 'or', 'elif', 'else']
    palabras_reservadas_ciclos = ['while', 'for', 'in', 'range']
    EI.PANTALLA.fill(EI.NEGRO)  #Se limpia la pantalla
    y = 0
    for line in lines:  #Se itera en cada línea
        x = EI.ancho * 0.005  #Posición horizontal inicial de la línea
        palabra_actual = ""  #Inicializamos una cadena vacía para construir cada palabra
        i = 0
        while i < len(line):
            char = line[i]
            if char in (" ", "\t", "(", ")", ",", ":", ";"):  #Si encontramos un delimitador
                if palabra_actual:  #Si hay una palabra para renderizar
                    if palabra_actual in palabras_reservadas:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.ROJO)  #Renderizar la palabra reservada en rojo
                    elif palabra_actual in palabras_reservadas_condicionales:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.AZUL)  #Renderizar la palabra reservada en azul
                    elif palabra_actual in palabras_reservadas_ciclos:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.VERDE)  #Renderizar la palabra reservada en verde
                    elif palabra_actual == 'def':
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.AMARILLO_FONDO)  #Renderizar la palabra reservada en amarillo
                    else:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.BLANCO)  #Renderizar la palabra en blanco
                    EI.PANTALLA.blit(palabra_renderizada, (x, y))  #Se muestra la palabra en la pantalla
                    x += fuente_codigo.size(palabra_actual)[0]  #Se ajusta la posición horizontal para la siguiente palabra
                    palabra_actual = ""  #Reiniciamos la palabra actual para la próxima palabra
                
                #Renderizar el delimitador
                delim_renderizado = fuente_codigo.render(char, True, EI.BLANCO)
                EI.PANTALLA.blit(delim_renderizado, (x, y))
                x += fuente_codigo.size(char)[0]  #Se ajusta la posición horizontal para el siguiente caracter
            else:
                palabra_actual += char  #Se agrega el caracter a la palabra actual
            i += 1
        
        #Renderizar la última palabra de la línea (si no hay delimitador al final)
        if palabra_actual:
            if palabra_actual in palabras_reservadas:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.ROJO)  #Renderizar la palabra reservada en rojo
            elif palabra_actual in palabras_reservadas_condicionales:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.AZUL)  #Renderizar la palabra reservada en azul
            elif palabra_actual in palabras_reservadas_ciclos:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.VERDE)  #Renderizar la palabra reservada en verde
            elif palabra_actual == 'def':
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.AMARILLO_FONDO)  #Renderizar la palabra reservada en amarillo        
            else:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, EI.BLANCO)  #Renderizar la palabra en blanco
            EI.PANTALLA.blit(palabra_renderizada, (x, y))  #Se muestra la palabra en la pantalla
            x += fuente_codigo.size(palabra_actual)[0]  #Se ajusta la posición horizontal para la siguiente palabra
        y += tamaño_fuente + EI.alto * 0.008  #Se ajusta la posición vertical para la siguiente línea

    #Se calcula la posición del cursor
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
            #Si se presiona 'Enter' luego de dos puntos, se salta de línea y se pone una tabulación
            indentation = len(current_line) - len(current_line.lstrip(' '))
            lines.insert(line + 1, " " * (indentation + 4))
            cursor_pos[0] += 1
            cursor_pos[1] = indentation + 4
        else: #Si se presiona 'Enter', se salta de línea
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
    render_text()
    pygame.display.flip()

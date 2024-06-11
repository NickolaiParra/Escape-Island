import pygame
import random
import multiprocessing
pygame.init()

#Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
VERDE_OSCURO = (41, 99, 14)
AZUL = (0, 0, 255)
FONDO = (244, 236, 223) 
H14AD8F = (20, 143, 173) 
GRIS = (155, 155, 155)
NARANJA = (255, 100, 0)
CIAN = (190,220,255)    
AMARILLO_FONDO = (255,168,100)
DORADO_FONDO = (251,192,34)
MORADO = (75, 12, 148)

#Pantalla
informacion_pantalla = pygame.display.Info() #Información sobre la pantalla
ancho = informacion_pantalla.current_w  #Información sobre el ancho de la pantalla
alto = informacion_pantalla.current_h  #Información sobre el alto de la pantalla
PANTALLA = pygame.display.set_mode((ancho, alto)) #Tamaño
pygame.display.set_caption("Escape Island") #Título
logo = pygame.image.load("Imagenes\Portada-Logo\Logo.png").convert()
pygame.display.set_icon(logo) #Logo

#Imágenes
portada = pygame.image.load("Imagenes\Portada-Logo\Portada.jpeg").convert()
portada_2 = pygame.image.load("Imagenes\Portada-Logo\Portada_2.jpeg").convert() 
mapa_avion = pygame.image.load("Imagenes\Mapa\Avion.png").convert()
pantalla_de_carga = pygame.image.load("Imagenes\Portada-Logo\Pantalla_de_carga.png").convert()
icono_sonido = pygame.image.load("Imagenes\Iconos\Sonido.png")
icono_sinsonido = pygame.image.load("Imagenes\Iconos\Sinsonido.png")
icono_brillo = pygame.image.load("Imagenes\Iconos\Brillo.png")
icono_sinbrillo = pygame.image.load("Imagenes\Iconos\Sinbrillo.png")
dialogo = pygame.image.load("Imagenes\Mapa\dialogo.png").convert()
flechas = pygame.image.load("Imagenes\Iconos\Flechas.png")
flecha_izquierda = pygame.image.load("Imagenes\Iconos\Flecha_izquierda.png")
flecha_derecha = pygame.image.load("Imagenes\Iconos\Flecha_derecha.png")
flecha_abajo = pygame.image.load("Imagenes\Iconos\Flecha_abajo.png")
flecha_arriba = pygame.image.load("Imagenes\Iconos\Flecha_arriba.png")
fondo_1 = pygame.image.load("Imagenes\Mapa\Fondo_1.png").convert()
fondo_2 = pygame.image.load("Imagenes\Mapa\Fondo_2.png").convert()
fondo_3 = pygame.image.load("Imagenes\Mapa\Fondo_3.png").convert()
shift = pygame.image.load("Imagenes\Iconos\Shift.png")
shift_flechaizquierda = pygame.image.load("Imagenes\Iconos\Shift_flecha_izquierda.png")
shift_flechaderecha = pygame.image.load("Imagenes\Iconos\Shift_flecha_derecha.png")
shift_izquierda = pygame.image.load("Imagenes\Iconos\Shift_izquierda.png")
shift_derecha = pygame.image.load("Imagenes\Iconos\Shift_derecha.png")
espacio_presionado = pygame.image.load("Imagenes/Iconos/Espacio_presionado.png")
espacio_sinpresionar = pygame.image.load("Imagenes/Iconos/Espacio_sin_presionar.png")
tecla_x = pygame.image.load("Imagenes/Iconos/X.png")
tecla_xpresionada = pygame.image.load("Imagenes/Iconos/X_presionada.png")
tecla_z = pygame.image.load("Imagenes/Iconos/Z.png")
tecla_zpresionada = pygame.image.load("Imagenes/Iconos/Z_presionada.png")
variably = pygame.image.load("Imagenes/Sprites/Variably.png").convert_alpha()
condi = pygame.image.load("Imagenes/Sprites/Condi.png").convert_alpha()
muerte = pygame.image.load("Imagenes/Sprites/Esqueleto.png").convert_alpha()
fondo_aldea = pygame.image.load("Imagenes/Mapa/Fondo_aldea.jpg").convert()
fondo_cueva = pygame.image.load("Imagenes/Mapa/Fondo_cueva.jpg").convert()
fondo_guerra = pygame.image.load("Imagenes/Mapa/Fondo_guerra.png").convert()
fondo_final = pygame.image.load("Imagenes/Mapa/Fondo_final.jpg").convert()
caja_a = pygame.image.load("Imagenes/Iconos/caja_a.png").convert()
caja_b = pygame.image.load("Imagenes/Iconos/caja_b.png").convert()
caja_c = pygame.image.load("Imagenes/Iconos/caja_c.png").convert()
caja_d = pygame.image.load("Imagenes/Iconos/caja_d.png").convert()
caja_a_rota = pygame.image.load("Imagenes/Iconos/caja_a_rota.png").convert()
caja_b_rota = pygame.image.load("Imagenes/Iconos/caja_b_rota.png").convert()
caja_c_rota = pygame.image.load("Imagenes/Iconos/caja_c_rota.png").convert()
caja_d_rota = pygame.image.load("Imagenes/Iconos/caja_d_rota.png").convert()
estrella_vacia = pygame.image.load("Imagenes/Iconos/Estrella_vacia.png")
estrella_rellena = pygame.image.load("Imagenes/Iconos/Estrella_rellena.png")

#Funciones

#Variables del editor

def render_text(cursor_pos, lines, fuente_codigo, tamaño_fuente):
    '''Esta función recibe como argumento la posición del cursor, una lista de palabras, la fuente y el tamaño del texto; y muestra el texto y el cursor de un editor de código'''
    # Lista con palabras reservadas importantes
    palabras_reservadas = ['True', 'False', 'print', 'input', 'abs', 'int', 'float', 'None']
    palabras_reservadas_condicionales = ['if', 'and', 'or', 'elif', 'else']
    palabras_reservadas_ciclos = ['while', 'for', 'in', 'range', "break", "continue"]
    palabras_reservadas_funciones = ['def', 'return']
    PANTALLA.fill(NEGRO)  #Se limpia la pantalla
    y = 0
    for line in lines:  #Se itera en cada línea
        x = ancho * 0.005  #Posición horizontal inicial de la línea
        palabra_actual = ""  #Inicializamos una cadena vacía para construir cada palabra
        i = 0
        while i < len(line):
            char = line[i]
            if char in (" ", "\t", "(", ")", ",", ":", ";"):  #Si encontramos un delimitador
                if palabra_actual:  #Si hay una palabra para renderizar
                    if palabra_actual in palabras_reservadas:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, ROJO)  #Renderizar la palabra reservada en rojo
                    elif palabra_actual in palabras_reservadas_condicionales:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, AZUL)  #Renderizar la palabra reservada en azul
                    elif palabra_actual in palabras_reservadas_ciclos:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, VERDE)  #Renderizar la palabra reservada en verde
                    elif palabra_actual in palabras_reservadas_funciones:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, AMARILLO_FONDO)  #Renderizar la palabra reservada en amarillo
                    else:
                        palabra_renderizada = fuente_codigo.render(palabra_actual, True, BLANCO)  #Renderizar la palabra en blanco
                    PANTALLA.blit(palabra_renderizada, (x, y))  #Se muestra la palabra en la pantalla
                    x += fuente_codigo.size(palabra_actual)[0]  #Se ajusta la posición horizontal para la siguiente palabra
                    palabra_actual = ""  #Reiniciamos la palabra actual para la próxima palabra
                
                #Renderizar el delimitador
                delim_renderizado = fuente_codigo.render(char, True, BLANCO)
                PANTALLA.blit(delim_renderizado, (x, y))
                x += fuente_codigo.size(char)[0]  #Se ajusta la posición horizontal para el siguiente caracter
            else:
                palabra_actual += char  #Se agrega el caracter a la palabra actual
            i += 1
        
        #Renderizar la última palabra de la línea (si no hay delimitador al final)
        if palabra_actual:
            if palabra_actual in palabras_reservadas:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, ROJO)  #Renderizar la palabra reservada en rojo
            elif palabra_actual in palabras_reservadas_condicionales:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, AZUL)  #Renderizar la palabra reservada en azul
            elif palabra_actual in palabras_reservadas_ciclos:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, VERDE)  #Renderizar la palabra reservada en verde
            elif palabra_actual in palabras_reservadas_funciones:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, AMARILLO_FONDO)  #Renderizar la palabra reservada en amarillo        
            else:
                palabra_renderizada = fuente_codigo.render(palabra_actual, True, BLANCO)  #Renderizar la palabra en blanco
            PANTALLA.blit(palabra_renderizada, (x, y))  #Se muestra la palabra en la pantalla
            x += fuente_codigo.size(palabra_actual)[0]  #Se ajusta la posición horizontal para la siguiente palabra
        y += tamaño_fuente + alto * 0.008  #Se ajusta la posición vertical para la siguiente línea

    #Se calcula la posición del cursor
    cursor_x = ancho * 0.005 + fuente_codigo.size(lines[cursor_pos[0]][:cursor_pos[1]])[0]
    cursor_y = cursor_pos[0] * tamaño_fuente + (alto * 0.008) * cursor_pos[0]
    pygame.draw.line(PANTALLA, BLANCO, (cursor_x, cursor_y), (cursor_x, cursor_y + tamaño_fuente), int(ancho * 0.0015))

def escape_island_base(x, y, salida_x, salida_y):
            """Esta función soluciona el examen final."""
            pasos = ""
            while (x, y) != (salida_x, salida_y):
                distancia_x = abs(x - salida_x)
                distancia_y = abs(y - salida_y)
                if distancia_x == 0:
                    pasos += 'y'
                    y = y - 1 if y > salida_y else y + 1
                elif distancia_y == 0:
                    pasos += 'x'
                    x = x - 1 if x > salida_x else x + 1
                elif distancia_x < distancia_y:
                    pasos += 'x'
                    x = x - 1 if x > salida_x else x + 1
                elif distancia_y < distancia_x:
                    pasos += 'y'
                    y = y - 1 if y > salida_y else y + 1
                else:
                    pasos += 'igual'
                    x = x - 1 if x > salida_x else x + 1
                    y = y - 1 if y > salida_y else y + 1
            pasos += 'salida'
            return pasos

t = ''
correcto = None
comprobacion = True
def keydown(cursor_pos, lines, lines_total, event):
    global t
    '''Esta función recibe como argumento la posición del cursor, la lista de palabras actual, la lista de palabras total y un evento de tipo KEYDOWN; y maneja los eventos en un editor de código'''
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
    elif key == pygame.K_LSHIFT or key == pygame.K_RSHIFT or key == pygame.K_CAPSLOCK:
        pass

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
        global correcto
        global comprobacion
        try:
            print(f"El código es: {lines_total}")
            complete_code = '\n'.join(sum(lines_total, []))
            print(complete_code)
            exec(complete_code, globals())
            #Ejecutar el código del jugador
            '''def ejecutar_codigo(code):
                exec(code, globals())

            if __name__ == "__main__":
                # Crea un proceso que ejecutará la función ejecutar_codigo
                p = multiprocessing.Process(target=ejecutar_codigo, args=(complete_code,))
                #Inicia el proceso
                p.start()
                #Espera durante 2 segundos o hasta que el proceso termine
                p.join(2)

                #Si el proceso todavía está en ejecución después de 2 segundos
                if p.is_alive():
                    print("El código se está ejecutando por demasiado tiempo, se detendrá.")
                    p.terminate()
                    p.join()
                    comprobacion = False
            if comprobacion:'''
            
            #100 casos de prueba aleatorios
            for _ in range(1, 101):
                salida_x = random.randint(1, 10)
                salida_y = random.randint(1, 10)
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                resultado_base = escape_island_base(x, y, salida_x, salida_y)
                resultado_jugador = escape_island(x, y, salida_x, salida_y)
                
                if resultado_jugador != resultado_base:
                    correcto = False
                    print("Discrepancia detectada:")
                    print(f"Entrada: x={x}, y={y}, salida_x={salida_x}, salida_y={salida_y}")
                    print(f"Resultado esperado: {resultado_base}")
                    print(f"Resultado del jugador: {resultado_jugador}")
                    break
                else: correcto = True
            if correcto:
                t = "¡Felicidades! Has completado el desafío."
            else:
                t = 'El código se ha ejecutado correctamente, pero el resultado es incorrecto.'''
        except:
           t = "Error al ejecutar el código."

    else:
        #Se agrega el caracter
        char = event.unicode
        lines[line] = current_line[:pos] + char + current_line[pos:]
        cursor_pos[1] += 1

def transicion_desvanecimiento(pantalla_carga, pantalla_inicio, tiempo_transicion):
    """Esta función realiza una transición de desvanecimiento. Recibe como argumentos la pantalla que se quiere cargar, la pantalla de inicio y el tiempo de transición (en milisegundos)"""
    #Se establecen dos superficies temporales en las que se copian la pantalla de carga y la pantalla de inicio
    pantalla_carga_surface = pygame.Surface((ancho, alto))
    pantalla_carga_surface.blit(pantalla_carga, (0, 0))

    pantalla_inicio_surface = pygame.Surface((ancho, alto))
    pantalla_inicio_surface.blit(pantalla_inicio, (0, 0))

    #Se itera desde 255 hasta 0 con decrementos de 5
    for alpha in range(255, 0, -5):
        pantalla_inicio_surface.set_alpha(alpha) #Se modifica la transparencia de pantalla_inicio hasta que sea transparente
        #Se limpia el fondo y se imprimen ambas pantallas
        PANTALLA.fill(FONDO) 
        PANTALLA.blit(pantalla_carga_surface, (0, 0))
        PANTALLA.blit(pantalla_inicio_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(tiempo_transicion // 50) #Se agrega un retraso para controlar la velocidad de transición

def cargar_sprites(hoja_sprites, ancho_sprite, alto_sprite, espacio_entre_sprites, ancho_sprite_resultante = ancho * 0.09, alto_sprite_resultante = alto * 0.09):
    """Esta función toma como argumento la hoja de sprites, el ancho de cada sprite, el alto de cada sprite, el espacio entre sprites, el ancho del sprite resultante, el alto del sprite resultante y retorna cada sprite separado individualmente en una lista"""
    sprites = []
    for x in range(0, hoja_sprites.get_width(), espacio_entre_sprites): #Se itera entre 0 y el ancho total de la hoja de sprites con un paso de espacio_entre_sprites
        #Se extrae un sprite individiual de la hoja de sprites y se almacena en sprites
        cuadro = hoja_sprites.subsurface((x, 0, ancho_sprite, alto_sprite)) 
        cuadro = pygame.transform.scale(cuadro, (ancho_sprite_resultante, alto_sprite_resultante)) #Se adecua el sprite a un tamaño específico 
        sprites.append(cuadro)
    return sprites

def dibujar_barra(pos_x, color_barra, color_control, color_anterior, x, y, ancho_barra, alto_barra, ancho_control, alto_control):
    """Esta función toma como argumentos la posición del cursor del mouse, el color de la barra, el color del control deslizante, el color anterior, la posición x de la barra, la posición y de la barra, el ancho de la barra, el alto de la barra, el ancho del control deslizante, el alto del control deslizante y dibuja una barra con control deslizante"""
    pygame.draw.rect(PANTALLA, color_anterior, (x, y, pos_x - x, alto_barra))  #Parte anterior de la barra
    pygame.draw.rect(PANTALLA, color_barra, (pos_x, y, ancho_barra - (pos_x - x), alto_barra))  #Parte posterior de la barra
    pygame.draw.rect(PANTALLA, color_control, (pos_x, y - (alto_control - alto_barra) / 2, ancho_control, alto_control))  #Control deslizante

def mostrar_texto(titulo, linea1, linea2 = "",linea3 = "", tamaño_titulo = int(ancho * 0.023), tamaño_texto = int(ancho * 0.02), color = NARANJA):
    """Esta función toma como argumentos el título, el texto de máximo 3 líneas, el tamaño del título, el tamaño del texto, el color del título y retorna un cuadro de texto en la parte inferior"""
    fuente_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf", tamaño_texto)
    personaje_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf", tamaño_titulo) 
    personaje_dialog.set_bold(True)
    dialog_char = personaje_dialog.render("Hola",True,NEGRO)
    dialog_char_rect = dialog_char.get_rect()
    dialog_char_rect.topright = (ancho * 0.1, alto * 0.74)
    dialog_text1 = fuente_dialog.render("Hola",True,NEGRO)
    dialog_text_rect1 = dialog_text1.get_rect()
    dialog_text_rect1.topright = (ancho * 0.1, alto * 0.80)
    dialog_text2 = fuente_dialog.render("Hola", True,NEGRO)
    dialog_text_rect2 = dialog_text1.get_rect()
    dialog_text_rect2.topright = (ancho * 0.1, alto * 0.85)
    dialog_text3 = fuente_dialog.render("Hola", True,NEGRO)
    dialog_text_rect3 = dialog_text1.get_rect()
    dialog_text_rect3.topright = (ancho * 0.1, alto * 0.90)
    dialframe = pygame.transform.scale(dialogo,(ancho, 0.3 * alto))
    dialframe_rect = dialframe.get_rect()
    dialframe_rect.bottomleft = (0,alto)
    PANTALLA.blit(dialframe,dialframe_rect)
    dialog_char = personaje_dialog.render(titulo, True, color)
    PANTALLA.blit(dialog_char,dialog_char_rect)
    dialog_text1 = fuente_dialog.render(linea1, True, NEGRO)
    PANTALLA.blit(dialog_text1,dialog_text_rect1)
    dialog_text2 = fuente_dialog.render(linea2, True, NEGRO)
    PANTALLA.blit(dialog_text2,dialog_text_rect2)
    dialog_text3 = fuente_dialog.render(linea3, True, NEGRO)
    PANTALLA.blit(dialog_text3,dialog_text_rect3)

def pregunta(titulo,pregunta,r1,r2,r3,r4, tamaño_texto =int(ancho * 0.02),tamaño_titulo =int(ancho * 0.023)):
    """Esta función toma como argumento el título del cuestionario, el texto de la pregunta, el texto de 4 respuestas, el tamaño del texto, el tamaño del título y retorna una plantilla de cuestionario usando cuatro cajas."""
    caja_a = pygame.image.load("Imagenes/Iconos/caja_a.png").convert()
    caja_b = pygame.image.load("Imagenes/Iconos/caja_b.png").convert()
    caja_c = pygame.image.load("Imagenes/Iconos/caja_c.png").convert()
    caja_d = pygame.image.load("Imagenes/Iconos/caja_d.png").convert()
    l1,l2,l3 = pregunta
    #Cajas
    caja_a = pygame.transform.scale(caja_a,(ancho * 0.1,alto * 0.15))
    caja_a_rect = caja_a.get_rect()
    caja_a_rect.bottomleft=(ancho * 0.25, alto * 0.69)
    caja_b = pygame.transform.scale(caja_b,(ancho * 0.1,alto * 0.15))
    caja_b_rect = caja_b.get_rect()
    caja_b_rect.bottomleft=(ancho * 0.4, alto * 0.69)
    caja_c = pygame.transform.scale(caja_c,(ancho * 0.1,alto * 0.15))
    caja_c_rect = caja_c.get_rect()
    caja_c_rect.bottomleft=(ancho * 0.55, alto * 0.69)
    caja_d = pygame.transform.scale(caja_d,(ancho * 0.1,alto * 0.15))
    caja_d_rect = caja_d.get_rect()
    caja_d_rect.bottomleft=(ancho * 0.7, alto * 0.69)
    mostrar_texto(titulo,l1,l2,l3,color=ROJO)
    fuente_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf", tamaño_texto)
    fuente_titulo = pygame.font.Font("Fuentes/Sedan-Regular.ttf", tamaño_titulo)
    
    titulo_pregunta = fuente_titulo.render(" Respuestas: ",True,ROJO)
    titulo_pregunta_rect = titulo_pregunta.get_rect()
    titulo_pregunta_rect.topleft =  (ancho * 0.19,alto*0.04)
    pygame.draw.rect(PANTALLA,DORADO_FONDO,titulo_pregunta_rect)
    pygame.draw.rect(PANTALLA,NEGRO,titulo_pregunta_rect,1)
    PANTALLA.blit(titulo_pregunta,titulo_pregunta_rect)
    
    resp_a = fuente_dialog.render((" a. "+ r1 + " "),True,NEGRO)
    resp_a_rect = resp_a.get_rect()
    resp_a_rect.topleft = (ancho * 0.2,alto*0.1)
    pygame.draw.rect(PANTALLA,AMARILLO_FONDO,resp_a_rect)
    pygame.draw.rect(PANTALLA,NEGRO,resp_a_rect,1)
    PANTALLA.blit(resp_a,resp_a_rect)
    
    resp_b = fuente_dialog.render((" b. "+ r2 + " "),True,NEGRO)
    resp_b_rect = resp_b.get_rect()
    resp_b_rect.topleft = (ancho * 0.2,alto*0.15)
    pygame.draw.rect(PANTALLA,AMARILLO_FONDO,resp_b_rect)
    pygame.draw.rect(PANTALLA,NEGRO,resp_b_rect,1)
    PANTALLA.blit(resp_b,resp_b_rect)
    
    resp_c = fuente_dialog.render((" c. "+ r3 + " "),True,NEGRO)
    resp_c_rect = resp_c.get_rect()
    resp_c_rect.topleft = (ancho * 0.2,alto*0.2)
    pygame.draw.rect(PANTALLA,AMARILLO_FONDO,resp_c_rect)
    pygame.draw.rect(PANTALLA,NEGRO,resp_c_rect,1)
    PANTALLA.blit(resp_c,resp_c_rect)
    
    resp_d = fuente_dialog.render((" d. "+ r4 + " "),True,NEGRO)
    resp_d_rect = resp_d.get_rect()
    resp_d_rect.topleft = (ancho * 0.2,alto*0.25)
    pygame.draw.rect(PANTALLA,AMARILLO_FONDO,resp_d_rect)
    pygame.draw.rect(PANTALLA,NEGRO,resp_d_rect,1)
    PANTALLA.blit(resp_d,resp_d_rect)
    
    PANTALLA.blit(caja_a,caja_a_rect)
    PANTALLA.blit(caja_b,caja_b_rect)
    PANTALLA.blit(caja_c,caja_c_rect)
    PANTALLA.blit(caja_d,caja_d_rect)

#Clases
class Boton:
    def __init__(self, x, y, ancho, alto, texto, tamaño, radio_esquinas):
        """Este método toma como parámetro la posición x, la posición y, el ancho, el alto, el texto, el tamaño del texto y el radio de las esquinas de un botón"""
        self.rect = pygame.Rect(x, y, ancho, alto) #Se crea un rectángulo usando las coordenadas (x, y) y las dimensiones ancho y alto
        self.color_normal = AZUL
        self.texto = texto
        self.radio_esquinas = radio_esquinas
        self.font = pygame.font.Font(None, tamaño) #Se crea un objeto de fuente
        self.render_texto = self.font.render(texto, True, BLANCO) #Se renderiza el texto usando la fuente definida previamente
        self.render_rect_texto = self.render_texto.get_rect(center=self.rect.center) #Se obtiene el rectángulo que rodea al texto y se centra dentro del rectángulo del botón
    def dibujar(self, pantalla):
        """Este método toma como parámetro la superficie en la que se va a mostrar el botón"""
        pygame.draw.rect(pantalla, self.color_normal, self.rect, border_radius=self.radio_esquinas) #Se dibuja un rectángulo según las condiciones de self.rect
        pantalla.blit(self.render_texto, self.render_rect_texto) #Se muestra el texto renderizado en la posición de self.render_rect_texto 
    def esta_encima(self, posicion):
        """Este método toma como argumento la posición del cursor del mouse"""
        return self.rect.collidepoint(posicion) #Se retorna True si la posición se encuentra dentro del rectángulo self.rect y False en caso contrario
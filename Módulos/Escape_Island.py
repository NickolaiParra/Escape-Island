import pygame
pygame.init()

#Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
FONDO = (244, 236, 223) 
H14AD8F = (20, 143, 173) 
GRIS = (155, 155, 155)
NARANJA = (255, 100, 0)
CIAN = (190,220,255)    
AMARILLO_FONDO = (255,168,100)
DORADO_FONDO = (251,192,34)

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
icono_sonido = pygame.image.load("Imagenes\Iconos\Sonido.png").convert()
icono_sinsonido = pygame.image.load("Imagenes\Iconos\Sinsonido.png").convert()
icono_brillo = pygame.image.load("Imagenes\Iconos\Brillo.png").convert()
icono_sinbrillo = pygame.image.load("Imagenes\Iconos\Sinbrillo.png").convert()
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
fondo_aldea = pygame.image.load("Imagenes/Mapa/Fondo_aldea.jpg").convert()
caja_a = pygame.image.load("Imagenes/Iconos/caja_a.png").convert()
caja_b = pygame.image.load("Imagenes/Iconos/caja_b.png").convert()
caja_c = pygame.image.load("Imagenes/Iconos/caja_c.png").convert()
caja_d = pygame.image.load("Imagenes/Iconos/caja_d.png").convert()
caja_a_rota = pygame.image.load("Imagenes/Iconos/caja_a_rota.png").convert()
caja_b_rota = pygame.image.load("Imagenes/Iconos/caja_b_rota.png").convert()
caja_c_rota = pygame.image.load("Imagenes/Iconos/caja_c_rota.png").convert()
caja_d_rota = pygame.image.load("Imagenes/Iconos/caja_d_rota.png").convert()

#Funciones
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
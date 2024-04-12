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

#Imágenes
logo = pygame.image.load("Imagenes\Portada-Logo\Logo.png") 
portada = pygame.image.load("Imagenes\Portada-Logo\Portada.jpeg") 
portada_2 = pygame.image.load("Imagenes\Portada-Logo\Portada_2.jpeg") 
mapa_avion = pygame.image.load("Imagenes\Mapa\Avion.png")
pantalla_de_carga = pygame.image.load("Imagenes\Portada-Logo\Pantalla_de_carga.png")

#Pantalla
informacion_pantalla = pygame.display.Info() #Información sobre la pantalla
ancho = informacion_pantalla.current_w  #Información sobre el ancho de la pantalla
alto = informacion_pantalla.current_h  #Información sobre el alto de la pantalla
PANTALLA = pygame.display.set_mode((ancho, alto)) #Tamaño
pygame.display.set_caption("Escape Island") #Título
pygame.display.set_icon(logo) #Logo

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

#Clases
class Boton:
    def __init__(self, x, y, ancho, alto, texto, tamaño):
        """Este método toma como parámetro la posición x, la posición y, el ancho, el alto, el texto de un botón y el tamaño del texto"""
        self.rect = pygame.Rect(x, y, ancho, alto) #Se crea un rectángulo usando las coordenadas (x, y) y las dimensiones ancho y alto
        self.color_normal = AZUL
        self.texto = texto
        self.font = pygame.font.Font(None, tamaño) #Se crea un objeto de fuente
        self.render_texto = self.font.render(texto, True, BLANCO) #Se renderiza el texto usando la fuente definida previamente
        self.render_rect_texto = self.render_texto.get_rect(center=self.rect.center) #Se obtiene el rectángulo que rodea al texto y se centra dentro del rectángulo del botón
    def dibujar(self, pantalla):
        """Este método toma como parámetro la superficie en la que se va a mostrar el botón"""
        pygame.draw.rect(pantalla, self.color_normal, self.rect) #Se dibuja un rectángulo según las condiciones de self.rect
        pantalla.blit(self.render_texto, self.render_rect_texto) #Se muestra el texto renderizado en la posición de self.render_rect_texto 
    def esta_encima(self, posicion):
        """Este método toma como argumento la posición del cursor del mouse"""
        return self.rect.collidepoint(posicion) #Se retorna True si la posición se encuentra dentro del rectángulo self.rect y False en caso contrario
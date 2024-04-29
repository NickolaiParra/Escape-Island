import pygame
import sys

pygame.init()
from Módulos import Escape_Island as EI

BLACK = (0,0,0)
ORANGE = (255,100,0)


#Booleanos
running = True
dialog_active = False


num_dialog = 0

#Función para mostrar una pregunta  
def pregunta(pregunta,r1,r2,r3,r4,correcta = 1):
    pass


#While principal
while running:
    #Fondo
    EI.PANTALLA.fill(EI.CIAN)
    
    #Diálogos
    if dialog_active and num_dialog == 1:
        personaje = "Variably"
        EI.mostrar_texto(personaje,"Hola.","Bienvenido a la aldea de las variables.")
    elif dialog_active and num_dialog == 2:
        EI.mostrar_texto(personaje,"Veo que estás perdido.", "Déjame ayudarte.")
    elif dialog_active and num_dialog == 3:
        EI.mostrar_texto(personaje,"Soy el jefe de la aldea de variables.", "Mi nombre es Variably.")
    elif dialog_active and num_dialog == 4:
        EI.mostrar_texto(personaje,"Para progresar por estos lados, necesitas aprender a programar variables.", "Pero, ¡no te preocupes!", "Yo te enseñaré.")
    elif dialog_active and num_dialog == 5:
        EI.mostrar_texto(personaje,"Aquí te explicaremos qué es una variable y cómo se usa.","Empecemos por lo básico.","¿Te parece?")
    elif dialog_active and num_dialog == 6:
        t1 = "Una variable es como un lugar en el que puedes almacenar cosas."
        t2 = "Esas cosas pueden ser números, cadenas de texto y otros tipos de datos."
        t3 = "Y son muy útiles, ya que puedes acceder a esa información cuando la necesites."
        EI.mostrar_texto(personaje,t1,t2,t3)
    
    #Eventos    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RIGHT and dialog_active:
                #Avanzar el diálogo
                num_dialog += 1
            elif event.key == pygame.K_LEFT and dialog_active:
                #Retroceder en el diálogo
                num_dialog -= 1
            elif event.key == pygame.K_m:
                #Activar/Desactivar diálogos
                #Pendiente de cambiar
                if dialog_active:
                    dialog_active = False
                else:
                    dialog_active = True
    
    pygame.time.Clock().tick(60)
    pygame.display.update()
    

pygame.quit()
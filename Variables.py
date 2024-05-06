import pygame
import sys

pygame.init()
from Módulos import Escape_Island as EI

BLACK = (0,0,0)
ORANGE = (255,100,0)
AMARILLO_FONDO = (255,168,100)
DORADO_FONDO = (251,192,34)


#Booleanos
running = True
dialog_continue = True


num_dialog = -1

#personajes
variably = pygame.image.load("Imagenes/Sprites/Variably.png").convert_alpha()
variably = pygame.transform.scale(variably,(EI.ancho*0.2,EI.alto*0.3))
variably_rect = variably.get_rect()
variably_rect.bottomleft = (EI.ancho*0.01,EI.alto*0.7)

#Fondos
fondo_aldea = pygame.image.load("Imagenes/Sprites/Fondo_aldea.jpg").convert()
fondo_aldea = pygame.transform.scale(fondo_aldea,(EI.ancho*0.8,EI.alto*0.7))
fondo_aldea_rect = fondo_aldea.get_rect()
fondo_aldea_rect.midtop = (EI.ancho//2, 0)

#Cajas
caja_a = pygame.image.load("Imagenes/Sprites/caja_a.png").convert()
caja_a = pygame.transform.scale(caja_a,(EI.ancho * 0.1,EI.alto * 0.15))
caja_a_rect = caja_a.get_rect()
caja_a_rect.bottomleft=(EI.ancho * 0.25, EI.alto * 0.69)
caja_b = pygame.image.load("Imagenes/Sprites/caja_b.png").convert()
caja_b = pygame.transform.scale(caja_b,(EI.ancho * 0.1,EI.alto * 0.15))
caja_b_rect = caja_b.get_rect()
caja_b_rect.bottomleft=(EI.ancho * 0.4, EI.alto * 0.69)
caja_c = pygame.image.load("Imagenes/Sprites/caja_c.png").convert()
caja_c = pygame.transform.scale(caja_c,(EI.ancho * 0.1,EI.alto * 0.15))
caja_c_rect = caja_c.get_rect()
caja_c_rect.bottomleft=(EI.ancho * 0.55, EI.alto * 0.69)
caja_d = pygame.image.load("Imagenes/Sprites/caja_d.png").convert()
caja_d = pygame.transform.scale(caja_d,(EI.ancho * 0.1,EI.alto * 0.15))
caja_d_rect = caja_d.get_rect()
caja_d_rect.bottomleft=(EI.ancho * 0.7, EI.alto * 0.69)

#Función para mostrar una pregunta  
def pregunta(titulo,pregunta,r1,r2,r3,r4, tamaño_texto =int(EI.ancho * 0.02),tamaño_titulo =int(EI.ancho * 0.023)):
    l1,l2,l3 = pregunta
    EI.mostrar_texto(titulo,l1,l2,l3,color=EI.ROJO,)
    fuente_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf", tamaño_texto)
    fuente_titulo = pygame.font.Font("Fuentes/Sedan-Regular.ttf", tamaño_titulo)
    
    titulo_pregunta = fuente_titulo.render(" Respuestas: ",True,EI.ROJO)
    titulo_pregunta_rect = titulo_pregunta.get_rect()
    titulo_pregunta_rect.topleft =  (EI.ancho * 0.19,EI.alto*0.04)
    pygame.draw.rect(EI.PANTALLA,DORADO_FONDO,titulo_pregunta_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,titulo_pregunta_rect,1)
    EI.PANTALLA.blit(titulo_pregunta,titulo_pregunta_rect)
    
    resp_a = fuente_dialog.render((" a. "+ r1 + " "),True,EI.NEGRO)
    resp_a_rect = resp_a.get_rect()
    resp_a_rect.topleft = (EI.ancho * 0.2,EI.alto*0.1)
    pygame.draw.rect(EI.PANTALLA,AMARILLO_FONDO,resp_a_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_a_rect,1)
    EI.PANTALLA.blit(resp_a,resp_a_rect)
    
    resp_b = fuente_dialog.render((" b. "+ r2 + " "),True,EI.NEGRO)
    resp_b_rect = resp_b.get_rect()
    resp_b_rect.topleft = (EI.ancho * 0.2,EI.alto*0.15)
    pygame.draw.rect(EI.PANTALLA,AMARILLO_FONDO,resp_b_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_b_rect,1)
    EI.PANTALLA.blit(resp_b,resp_b_rect)
    
    resp_c = fuente_dialog.render((" c. "+ r3 + " "),True,EI.NEGRO)
    resp_c_rect = resp_c.get_rect()
    resp_c_rect.topleft = (EI.ancho * 0.2,EI.alto*0.2)
    pygame.draw.rect(EI.PANTALLA,AMARILLO_FONDO,resp_c_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_c_rect,1)
    EI.PANTALLA.blit(resp_c,resp_c_rect)
    
    resp_d = fuente_dialog.render((" d. "+ r4 + " "),True,EI.NEGRO)
    resp_d_rect = resp_d.get_rect()
    resp_d_rect.topleft = (EI.ancho * 0.2,EI.alto*0.25)
    pygame.draw.rect(EI.PANTALLA,AMARILLO_FONDO,resp_d_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_d_rect,1)
    EI.PANTALLA.blit(resp_d,resp_d_rect)
    
    EI.PANTALLA.blit(caja_a,caja_a_rect)
    EI.PANTALLA.blit(caja_b,caja_b_rect)
    EI.PANTALLA.blit(caja_c,caja_c_rect)
    EI.PANTALLA.blit(caja_d,caja_d_rect)


#While principal
while running:
    #Fondo
    EI.PANTALLA.fill((0,0,0))
    EI.PANTALLA.blit(fondo_aldea,fondo_aldea_rect)
    
    
    #Diálogos
    if num_dialog == -1:
        EI.mostrar_texto("Escape Island","Llegando a Aldea de las variables.","(Presiona 'Enter' para continuar)",color=EI.AZUL)
    elif num_dialog == 0:
        t1 = "Haz llegado a una aldea maravillosa"
        t2 = "Un aura de variabilidad llena el ambiente"
        t3 = "Sientes como tu gran aventura empieza de verdad."
        EI.mostrar_texto("Aldea de las variables",t1,t2,t3,color=EI.AZUL)
    elif num_dialog == 1:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "???"
        EI.mostrar_texto(personaje,"Hola.","Bienvenido a la aldea de las variables.")
    elif num_dialog == 2:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "???"
        EI.mostrar_texto(personaje,"Veo que estás perdido.", "Déjame ayudarte.")
    elif num_dialog == 3:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        EI.mostrar_texto(personaje,"Soy el jefe de la aldea de variables.", "Mi nombre es Variably.")
    elif num_dialog == 4:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        EI.mostrar_texto(personaje,"Para progresar por estos lados, necesitas aprender a programar variables.", "Pero, ¡no te preocupes!", "Yo te enseñaré.")
    elif num_dialog == 5:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        EI.mostrar_texto(personaje,"Aquí te explicaremos qué es una variable y cómo se usa.","Empecemos por lo básico.","¿Te parece?")
    elif num_dialog == 6:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Una variable es como un lugar en el que puedes almacenar cosas."
        t2 = "Esas cosas pueden ser números, cadenas de texto y otros tipos de datos."
        t3 = "Y son muy útiles, ya que puedes acceder a esa información cuando la necesites."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 7:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Por lo que una variable no es más que un espacio para guardar."
        t2 = "Uno en el que guardas información que necesites para hacer lo que tengas que hacer después."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 8:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Eso sería el concepto básico de una variable."
        t2 = "Este es el fin de tu primera lección."
        t3 = "Te voy a hacer una pregunta para ver si entendiste."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 9:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Te voy a dar una pregunta con 4 respuestas."
        t2 = "Selecciona la que más te parezca."
        t3 = "Para seleccionarla rompe la caja con 'x' o 'z'."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 10:
        #Quiz de variables 1
        EI.PANTALLA.blit(variably,variably_rect)
        t1 = "¿Qué es una variable en programación?"
        a = "Una caja"
        b = "Un espacio para guardar información"
        c = "Un valor numérico"
        d = "Una cadena de texto"
        correcta = 2
        pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
        dialog_continue = False
        #Cuando se responda correctamente:
        #dialog_continue debe volver a True
        #se le debe sumar 1 a num_dialog
    elif num_dialog == 11:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Bien hecho joven aventurero."
        t2 = "Haz completado exitosamente el primer paso para dominar las variables."
        t3 = "Ya que aprendimos la parte teórica, veamos como se aplica."
        EI.mostrar_texto(personaje,t1,t2,t3)
        #Siguen los diálogos del segundo tutorial
        
    else:
        EI.mostrar_texto("","")
    
    #Eventos    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RETURN and dialog_continue:
                #Avanzar el diálogo
                num_dialog += 1
    
    pygame.time.Clock().tick(60)
    pygame.display.update()
    

pygame.quit()
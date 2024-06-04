import pygame
import sys

pygame.init()
from Módulos import Escape_Island as EI

#Booleanos
running = True
dialog_continue = True


num_dialog = -1

#personajes
variably = pygame.transform.scale(EI.variably,(EI.ancho*0.2,EI.alto*0.3))
variably_rect = variably.get_rect()
variably_rect.bottomleft = (EI.ancho*0.01,EI.alto*0.7)

#Fondos

fondo_aldea = pygame.transform.scale(EI.fondo_aldea,(EI.ancho*0.8,EI.alto*0.7))
fondo_aldea_rect = fondo_aldea.get_rect()
fondo_aldea_rect.midtop = (EI.ancho//2, 0)

#Cajas
caja_a = pygame.transform.scale(EI.caja_a,(EI.ancho * 0.1,EI.alto * 0.15))
caja_a_rect = caja_a.get_rect()
caja_a_rect.bottomleft=(EI.ancho * 0.25, EI.alto * 0.69)
caja_b = pygame.transform.scale(EI.caja_b,(EI.ancho * 0.1,EI.alto * 0.15))
caja_b_rect = caja_b.get_rect()
caja_b_rect.bottomleft=(EI.ancho * 0.4, EI.alto * 0.69)
caja_c = pygame.transform.scale(EI.caja_c,(EI.ancho * 0.1,EI.alto * 0.15))
caja_c_rect = caja_c.get_rect()
caja_c_rect.bottomleft=(EI.ancho * 0.55, EI.alto * 0.69)
caja_d = pygame.transform.scale(EI.caja_d,(EI.ancho * 0.1,EI.alto * 0.15))
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
    pygame.draw.rect(EI.PANTALLA,EI.DORADO_FONDO,titulo_pregunta_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,titulo_pregunta_rect,1)
    EI.PANTALLA.blit(titulo_pregunta,titulo_pregunta_rect)
    
    resp_a = fuente_dialog.render((" a. "+ r1 + " "),True,EI.NEGRO)
    resp_a_rect = resp_a.get_rect()
    resp_a_rect.topleft = (EI.ancho * 0.2,EI.alto*0.1)
    pygame.draw.rect(EI.PANTALLA,EI.AMARILLO_FONDO,resp_a_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_a_rect,1)
    EI.PANTALLA.blit(resp_a,resp_a_rect)
    
    resp_b = fuente_dialog.render((" b. "+ r2 + " "),True,EI.NEGRO)
    resp_b_rect = resp_b.get_rect()
    resp_b_rect.topleft = (EI.ancho * 0.2,EI.alto*0.15)
    pygame.draw.rect(EI.PANTALLA,EI.AMARILLO_FONDO,resp_b_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_b_rect,1)
    EI.PANTALLA.blit(resp_b,resp_b_rect)
    
    resp_c = fuente_dialog.render((" c. "+ r3 + " "),True,EI.NEGRO)
    resp_c_rect = resp_c.get_rect()
    resp_c_rect.topleft = (EI.ancho * 0.2,EI.alto*0.2)
    pygame.draw.rect(EI.PANTALLA,EI.AMARILLO_FONDO,resp_c_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_c_rect,1)
    EI.PANTALLA.blit(resp_c,resp_c_rect)
    
    resp_d = fuente_dialog.render((" d. "+ r4 + " "),True,EI.NEGRO)
    resp_d_rect = resp_d.get_rect()
    resp_d_rect.topleft = (EI.ancho * 0.2,EI.alto*0.25)
    pygame.draw.rect(EI.PANTALLA,EI.AMARILLO_FONDO,resp_d_rect)
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
        EI.mostrar_texto("Escape Island","Llegando a la aldea de las variables.","(Usa las flechas para continuar).",color=EI.ROJO)
    elif num_dialog == 0:
        t1 = "Haz llegado a una aldea maravillosa."
        t2 = "Un aura de variabilidad llena el ambiente."
        t3 = "Sientes como tu gran aventura empieza de verdad."
        EI.mostrar_texto("Aldea de las variables",t1,t2,t3,color=EI.VERDE_OSCURO)
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
        a = "Una caja."
        b = "Un espacio para guardar información."
        c = "Un valor numérico."
        d = "Una cadena de texto."
        correcta = 2
        pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
        #dialog_continue = False
    elif num_dialog == -100: # Si se equivoca
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Eso no es correcto."
        t2 = "Vamos a volver a repasar el concepto clave"
        EI.mostrar_texto(personaje,t1,t2)
        #Vuelve a num_dialog == 6
    elif num_dialog == 11: # Si responde correctamente
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Bien hecho joven aventurero."
        t2 = "Haz completado exitosamente el primer paso para dominar las variables."
        t3 = "Ya que aprendimos la parte teórica, veamos como se aplica."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 12:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Para esto vamos a usar un lenguaje de programación que se llama Python."
        t2 = "Ya verás que es bastante intuitivo y fácil de usar."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 13:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Para hacer una variable primero debes ponerle un nombre."
        t2 = "Generalmente el nombre que le pones está relacionado con lo que guarda dentro."
        t3 = "Pero le puedes poner el nombre que más te parezca."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 14:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Por ejemplo, si vas a asignar un nombre a una variable, puedes poner:"
        t2 = "nombre = 'Juan'"
        t3 = "Y así se guarda 'Juan' en la variable 'nombre'"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 15:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "También, puedes guardar números de la siguente manera:"
        t2 = "numero_entero = 42"
        t3 = "numero_decimal = -3.1416"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 16:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "El último tipo de dato simple que puedes guardar es un booleano."
        t2 = "Este dato es un valor que puede ser verdadero o falso."
        t3 = "El valor de verdadero se escribe como 'True' y falso como 'False'"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 17:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Un ejemplo de esto es el siguiente:"
        t2 = "valor = True"
        t3 = "No se te olvide que los booleanos van en mayúscula en Python."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 17:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Esos son los tipos más sencillos de datos que vas a encontrar."
        t2 = "Y ya sabes como guardarlos en una variable para poder trabajar con ellos después."
        t3 = "Durante tu viaje seguirás usándolos y aprendiendo sobre estos."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 18:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Eso es todo por tu segunda y última lección aquí en la aldea."
        t2 = "Te voy a hacer una pregunta para ver si entendiste bien la lección."
        t3 = "¡Aquí vamos!"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 19:
        #Quiz de variables 2
        EI.PANTALLA.blit(variably,variably_rect)
        t1 = "Si yo quiero crear una variable que se llame 'fruta' y que guarde mi fruta favorita,"
        t2 = "¿Cuál de las siguentes es la forma correcta de nombrar la variable?"
        t3 = "Ten en cuenta la manera en la que están escritas."
        a = "'fresa' = fruta"
        b = "'fruta' = manzana"
        c = "kiwi = 'fruta'"
        d = "fruta = 'banana'"
        correcta = 4
        pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
        #dialog_continue = False
    elif num_dialog == -200: # Si se equivoca
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Eso no es correcto."
        t2 = "Devólvamonos para repasarlo."
        EI.mostrar_texto(personaje,t1,t2)
        #Vuelve a num_dialog == 13
    elif num_dialog == 20: # Si responde correctamente
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Muy bien."
        t2 = "Me queda claro que estás dominando el arte de crear variables."
        t3 = "Solo falta una última cosa que hacer."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 21:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Te vas a enfrentar al mayor reto que hayas visto hasta el momento"
        t2 = "Voy a hacerte 5 preguntas sobre lo que aprendiste hasta ahora."
        t3 = "Estarás solo y después vendré a ver cómo te fue."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 22:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Si pasas podrás irte."
        t2 = "Si no, entonces tu tiempo aquí se alargará."
        t3 = "¿Estás listo?"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 23:
        #Examen de variables
        #Pregunta 1
        t1 = "¿Para qué sirve una variable?"
        a = "Para guardar información."
        b = "Para hacer que un número varíe."
        c = "Para despejar una ecuación matemática."
        d = "Para ejecutar código."
        correcta = 1
        pregunta("Examen de variables",[t1,"",""],a,b,c,d)
    elif num_dialog == 24:
        #Pregunta 2
        t1 = "¿Cuál es la sintaxis corecta para definir una variable en Python?"
        a = "variable = valor"
        b = "valor = variable"
        c = "variable == valor"
        d = "valor == variable"
        correcta = 3
        pregunta("Examen de variables",[t1,"",""],a,b,c,d)
    elif num_dialog == 25:
        #Pregunta 3
        t1 = "Si se define la siguiente variable:"
        t2 = "ejecutando = True"
        t3 = "¿De qué tipo es la información qué guarda?"
        a = "Texto"
        b = "Booleano"
        c = "Número entero"
        d = "Número decimal"
        correcta = 2
        pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 26:
        #Pregunta 4
        t1 = "¿A qué corresponde el valor de la variable 'dulces' en el siguiente código?"
        t2 = "dulces = True"
        t3 = "dulces = 32"
        a = "32"
        b = "True"
        c = "None"
        d = "True 32"
        correcta = 1
        pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 27:
        #Pregunta 5
        t1 = "¿Cuál es el nombre del lenguaje de programación que se hemos estado usando?"
        a = "C++"
        b = "Java"
        c = "Python"
        d = "C"
        correcta = 3
        pregunta("Examen de variables",[t1,"",""],a,b,c,d)
    elif num_dialog == -300: # Si no pasa
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Lo intentaste."
        t2 = "No pierdas la esperanza."
        t3 = "Lo intentaremos otra vez."
        EI.mostrar_texto(personaje,t1,t2,t3)
        #Vuelve a num_dialog == 13
    elif num_dialog == 28: # Si pasa
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Felicidades."
        t2 = "Eres un maestro de las variables."
        t3 = "Te deseo lo mejor aventurero."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 29:
        EI.PANTALLA.blit(variably,variably_rect)
        personaje = "Variably"
        t1 = "Ya puedes proseguir con tu camino."
        EI.mostrar_texto(personaje,t1)
    elif num_dialog == 30:
        EI.mostrar_texto("Escape Island","Saliendo de la aldea de variables",color=EI.AZUL)
    elif num_dialog == 31:
        EI.mostrar_texto("","")
        #Vuelve al mapa principal
    else:
        EI.mostrar_texto("","")
    
    #Eventos    
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
    
    pygame.time.Clock().tick(60)
    pygame.display.update()
    

pygame.quit()
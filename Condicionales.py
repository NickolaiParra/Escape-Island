import pygame
import sys

pygame.init()
from Módulos import Escape_Island as EI

#Booleanos
running = True
dialog_continue = True


num_dialog = -1

#personajes
condi = pygame.transform.scale(EI.condi,(EI.ancho*0.2,EI.alto*0.3))
condi_rect = condi.get_rect()
condi_rect.bottomleft = (EI.ancho*0.01,EI.alto*0.7)

#Fondos

fondo_cueva = pygame.transform.scale(EI.fondo_cueva,(EI.ancho*0.8,EI.alto*0.7))
fondo_cueva_rect = fondo_cueva.get_rect()
fondo_cueva_rect.midtop = (EI.ancho//2, 0)

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
    EI.PANTALLA.blit(fondo_cueva,fondo_cueva_rect)
    
    
    #Diálogos
    if num_dialog == -1:
        EI.mostrar_texto("Escape Island","Llegando a la cueva de condicionales.",color=EI.ROJO)
    elif num_dialog == 0:
        t1 = "Haz llegado a una cueva intrigante."
        t2 = "El aire misterioso te condiciona a seguir."
        EI.mostrar_texto("Cueva de condicionales",t1,t2,color=EI.MORADO)
    elif num_dialog == 1:
        EI.mostrar_texto("Cueva de condicionales","Te tropiezas.","Haces un alboroto.","Si alguien te escuchara, estarías en problemas.",color=EI.MORADO)
    elif num_dialog == 2:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "???"
        EI.mostrar_texto(personaje,"¿¿¿Hay alguien ahí???", "Si es así...","Muéstrate!")
    elif num_dialog == 3:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Ah, pero sí eres un joven aventurero."
        t2 = "¿Qué te trae por estos lares tan silenciosos?"
        t3 = "Soy Condi, viejo maestro de las condiciones."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 4:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "¿Qué?"
        t2 = "Así que vienes de la aldea de las variables, ¿eh?"
        t3 = "En busca de llenar tu mente de sabiduría."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 5:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Si has venido a aprender, entonces estás en el lugar correcto."
        t2 = "Si no estoy mal, ya deberías saber sobre las variables."
        t3 = "Así que te podría enseñar mi especialidad: las condiciones."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 6:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Si estás listo..."
        t2 = "¡Comencemos de una vez!"
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 7:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Los condicionales son una de las herramientas más importantes en programación."
        t2 = "Te serán de mucha utilidad."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 8:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Para ponerte en contexto te voy a mostrar la estructura de un condicional:"
        t2 = "Si se cumple (condición) entonces:"
        t3 = "    se ejecuta (código)"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 9:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Básicamente, esto significa que si se cumple la condición que tú le pongas:"
        t2 = "Se ejecuta todo lo que tengas dentro de ese condicional."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 9:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Ahora te pregutarás"
        t2 = "¿Qué tipo de condiciones puedes poner?"
        t3 = "Bueno, es algo bastante sencillo."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 10:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Puedes comparar dos valores distintos."
        t2 = "Por ejemplo, puedes comparar 2 > 9 (2 es mayor que 9)"
        t3 = "Eso sería falso, por lo que no se ejecutaría la condición."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 11:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "También podemos poner:"
        t2 = "a = 10"
        t3 = "Y evaluar la condición a >= 10 (La variable a es mayor o igual a 10)"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 12:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Esto sería verdadero, ya que como a es 10 y 10 >= 10, entonces se cumple la condición."
        t2 = "Y todo lo que tengas dentro del condicional se ejecutaría."
        t3 = "No se te olvide que puedes comparar variables (lo que suele ser muy usado)."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 13:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Digamos que tienes dos varibles a = 10 y b = 20"
        t2 = "a == b (a es igual a b) sería falso, porque 10 == 20 (10 es igual a 20) es falso"
        t3 = "Y así puedes comparar variables."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 14:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Pero no sólo puedes comparar números."
        t2 = "También puedes comparar cadenas de texto (strings)."
        t3 = "Por ejemplo..."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 15:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Si tienes nombre = 'Variably' y jefe = 'Variably'."
        t2 = "Decir jefe == nombre es verdadero, ya que las dos contienen el mismo texto ('Variably')."
        t3 = "A parte de esto, puedes tener condiciones con booleanos."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 16:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Los booleanos son valores de Falso o Verdadero que se pueden usar en una condición."
        t2 = "Si tienes la variable condicion = True."
        t3 = "Cuando evalúes la condición en un condicional, el código se va a ejecutar."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 17:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Lo mismo sucede con False."
        t2 = "Si tienes condición = False."
        t3 = "No se va a ejecutar el código."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 18:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Algo interesante es que puedes poner varias condiciones en un mismo condicional."
        t2 = "Esto se hace con los operadores lógicos 'y' (and) y 'o' (or)."
        t3 = "Si has trabajado con lógica antes se te va a hacer un poco más fácil, ya que funcionan igual."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 19:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Si tenemos una variable a = True y otra variable b = False"
        t2 = "Al usar el operador de 'and', las dos condiciones tienen que ser verdadares para que se cumpla."
        t3 = "Por ejemplo: 'a and b' es falso, debido a que b es falso (False)."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 20:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Al igual que con 'and' se puede usar 'or'."
        t2 = "La diferencia es que 'or' solo necesita que una de las dos condiciones sea verdadera para funcionar."
        t3 = "Siguiendo el ejemplo anterior, 'a or b' sería verdadero, dado que a es verdadero (True)."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 21:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Cabe destacar que la condición puede ser una comparación de valores."
        t2 = "Si tomamos a = 10, b = 20 y c = 30, y tenemos 'a > b or c > b'"
        t3 = "Sería verdadero porque c > b es verdadero, aunque a > b no lo sea."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 22:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Eso sería la teoría de cómo funciona un condicional."
        t2 = "Si necesitas puedes volver para revisar algo de lo que dije. Es bastante información."
        t3 = "Bueno, veamos qué tanto aprendiste."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 23: # Quiz de concionales 1
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Si tenemos: a = 50, b = 20, c = 70"
        t2 = "Y la condición 'a > b and c >= a'"
        t3 = "¿La condición se cumple?"
        a = "Sí, todo se cumple"
        b = "No, nada se cumple"
        c = "No, solo se cumple a > b"
        d = "No, solo se cumple c >= a"
        pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
    elif num_dialog == -100: # Si falla
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Eso está mal."
        t2 = "Volvamos a ver."
        t3 = "Recuerda que no hay prisa."
        EI.mostrar_texto(personaje,t1,t2,t3)
        #Vuelve a num_dialog = 7
    elif num_dialog == 24: # Si responde bien
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Muy bien joven, ya lo estás entendiendo."
        t2 = "Sigamos con la siguiente lección."
        t3 = "Cómo aplicarlo."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 25:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Para aplicar los condicionales en Python se usa la siguiente estructura:"
        t2 = "if (condición):"
        t3 = "    (código)"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 26:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Bastante sencillo, no?"
        t2 = "Es lo mismo que aprendimos sobre las condiciones."
        t3 = "Solo que el código que se ejucuta dentro del condicional tiene que estar indentado."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 27:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "¿Que qué es indentado?"
        t2 = "Mira lo sencillo que es."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 28:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Significa que al principio de la línea tienes que dejar unos espacios."
        t2 = "Para hacerlo puedes dejar 4 espacios o presionar la tecla TAB."
        t3 = "Esto con el objetivo de indicar cuáles instrucciones se deben ejecutar si la condición es verdadera."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 29:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Por ejemplo, si tienes la variable edad y tipo_persona puedes hacer lo siguiete:"
        t2 = "if edad < 18:"
        t3 = "    tipo_persona = 'Menor de edad'"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 30:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Pero, ¿qué pasa si en el ejemplo anterior también queremos considerar a las personas mayores de edad?"
        t2 = "Tendríamos qué hacer otro condicional, ¿cierto?"
        t3 = "Pero también existe otra forrma de hacerlo."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 31:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Existe dos estructuras que son 'elif' y 'else'"
        t2 = "Estás se evalúan si la primera condición no se cumplió."
        t3 = "¿Pero cuál es la diferencia entre ellas?"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 32:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Básicamente, con 'elif' puedes escribir una segunda condición de la siguiente manera:"
        t2 = "elif (segunda condición):"
        t3 = "    (segundo código)"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 33:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Y lo interesante de esto es que 'elif' lo puedes usar cuantas veces quieras."
        t2 = "Una tercera, cuarta, décima vez o las veces que quieras."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 34:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "En cambio 'else' lo que hace es que si ninguna condición de las anteriores (incluyendo 'elif's)"
        t2 = "se ejecuta, entonces ejecuta lo que tiene el 'else'."
        t3 = "Volviendo al ejemplo de la edad, podríamos decir:"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 35:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "if 0 <= edad < 18: tipo_persona = 'Menor de edad'"
        t2 = "elif edad > 18: tipo_persona = 'Mayor de edad'"
        t3 = "else: tipo_persona = 'Inexistente'"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 36:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "En la primera condición evaluamos si la edad es menor a 18 y mayor o igual a cero."
        t2 = "Esto se hace para averiguar las personas menores de edad y verficar que la edad no sea negativa."
        t3 = "Una edad negativa no sería posible."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 37:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Luego, con el 'elif' evaluamos a las personas que tienen más de 18."
        t2 = "A estas les asignamos la mayoría de edad."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 38:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Por último, si nada se cumple significaría que tiene edad negativa."
        t2 = "Lo cual no es posible."
        t3 = "Por esto se le asigna la categoría de 'inexistente'."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 39:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Con este ejemplo creo que puedes dar un vistazo de todas las cosas que se pueden hacer con"
        t2 = "los condicionales."
        t3 = "¡Vayamos a la pregunta de la lección!"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 40: # Quiz de concionales 2
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "¿Para qué sirve indentar?"
        t2 = ""
        t3 = ""
        a = "Para indicar qué parte del código se debe ejecutar si se cumple la condición."
        b = "Para indicar que el código no se tiene que ejecutar."
        c = "Para tener una mejor organización en el código."
        d = "La a y la c."
        pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
    elif num_dialog == -200: # Si falla
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Eso no está bien."
        t2 = "Veamos qué pasó."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
        #Vuelve a num_dialog = 25
    elif num_dialog == 41: # Si responde bien
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Excelente, jóven."
        t2 = "Haz adquirido un gran conocimiento."
        t3 = "Veamos cómo te enfrentas a lo siguiente."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 42: 
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Aquí comienza tu prueba final."
        t2 = ""
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 43:
        #Examen de condicionales
        #Pregunta 1
        t1 = "¿Para qué sirve un condicional?"
        t2 = ""
        t3 = ""
        a = "Para guardar una parte del código."
        b = "Para ejecutar un código cuando se cumpla una condición específica."
        c = "Para almacenar información sobre las variables."
        d = "Para únicamente comparar dos números o cadenas."
        pregunta("Exámen de condicionales",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 44:
        #Pregunta 2
        t1 = "¿Cuál es la estructura de un condicional en Python?"
        t2 = ""
        t3 = ""
        a = "if (condición): (código)"
        b = "(código): if (condición)"
        c = "(condición): if (código)"
        d = "if (código): (condición)"
        pregunta("Exámen de condicionales",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 45:
        #Pregunta 3
        t1 = "Si tenemos a = True, b = 10 y c = 5,"
        t2 = "¿la siguiente condición se cumple?"
        t3 = "'a and b > c'"
        a = "Sí, todo se cumple."
        b = "No, porque solo 'a' es falso."
        c = "No, porque solo no se cumple 'b > c'."
        d = "No, todo es falso."
        pregunta("Exámen de condicionales",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 46:
        #Pregunta 4
        t1 = "Si tenemos a = False, b = True, c = 'manzana' d = 'Manzana',"
        t2 = "¿la siguiente condición se cumple?"
        t3 = "'(a or b) and (c == d)'"
        a = "Sí, todo se cumple."
        b = "No, porque solo '(a or b)' no se cumple."
        c = "No, porque solo '(c == d)' no se cumple."
        d = "No, porque ni '(a or b)' ni '(c == d)' se cumplen."
        pregunta("Exámen de condicionales",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 47:
        #Pregunta 5
        t1 = "¿Qué se usa para ejecutar un código, cuando la primera condición es falsa?"
        t2 = ""
        t3 = ""
        a = "'else' y 'elif'"
        b = "'print' y 'else'"
        c = "'if' y 'else'"
        d = "'print' e 'if'"
        pregunta("Exámen de condicionales",[t1,t2,t3],a,b,c,d)
    elif num_dialog == -300: # Si falla
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Tú puedes."
        t2 = "Vuelve a intentarlo."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
        #Vuelve a num_dialog = 25
    elif num_dialog == 48: #Si pasa
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "Increíble joven."
        t2 = "¡Has superado todas mis expectativas!"
        t3 = "Sigue tu camino."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 49:
        EI.PANTALLA.blit(condi,condi_rect)
        personaje = "Condi"
        t1 = "¡Un futuro grandioso te espera!"
        t2 = ""
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 50:
        t1 = "Saliendo de la cueva de condicionales."
        t2 = ""
        t3 = ""
        EI.mostrar_texto("Escape Island",t1,t2,t3, color=EI.ROJO)
        
        
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
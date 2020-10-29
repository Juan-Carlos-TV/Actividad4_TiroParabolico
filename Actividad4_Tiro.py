from random import randrange
from turtle import *
from freegames import vector

#Posición inical de la bola
ball = vector(-200, -200)
#Velocidad inicial de la bola
speed = vector(0, 0)
#Inicializar el arreglo de targets
targets = []

#Función que lee el click de la pantalla
def tap(x, y):
    "Respond to screen tap."
    #Verifica que no existe una bola
    if not inside(ball):
        #Cambia la posición de la bola a una válida
        ball.x = -199
        ball.y = -199
        #Establece una velocidad a partir de donde se
            #haya hecho click.
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

#Función que retorna True si determinadas coordenadas están
        #dentro de la pantalla
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Función de dibujo
def draw():
    "Draw ball and targets."
    #Limpia la pantalla
    clear()

    #Para cada elemento en targets
    for target in targets:
        #Se posiciona en la coordenada y dibuja un
            #círculo azul de 20 px
        goto(target.x, target.y)
        dot(20, 'blue')

    #Si hay una bola dentro de los límites la dibuja
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
    
    #Actualiza la pantalla
    update()

#Función para el movimiento de la bola y los targets
def move():
    "Move ball and targets."
    #Genera numeros aleatorios entre 0 y 40. Cuando el número
        #se igual a 0, genera un nuevo target
    #Si se desea generar targets más rápido disminuye este número
    #Si se desea generar targets menos rápido, se aumenta
    if randrange(40) == 0:
        #Genera una posición random de altura entre -150 y 150
        y = randrange(-150, 150)
        #Crea el target a la altura determinada y en el borde izq
        target = vector(200, y)
        #Añade al arreglo de targets
        targets.append(target)

    #Mueve cada uno de los targets 0.25 a la izquierda
    for target in targets:
        target.x -= 0.25

    #Cambia la velocidad en y, con una desaceleración
        #esta desaceleración genera el efecto de tiro parabólico
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    #Genera una copia del arreglo de targets
    dupe = targets.copy()
    #Vacía el arreglo de targets
    targets.clear()

    #Para cada target en dupe
    for target in dupe:
        #Verifica que ninguno de los targets haya sido tocado
            #por la bola. Si esto se cumple, los mete devuelta al
            #arreglo
        if abs(target - ball) > 13:
            targets.append(target)
            
    #Llama a draw
    draw()

    #Ahora el juego no acaba
    for target in targets:
        #Si las bolas salen, las reposiciona al otro lado
        if not inside(target):
            target.x = 200
    
    ontimer(move, 10)

#Establece el tamaño de la pantalla y su posición
setup(420, 420, 370, 0)
#Esconde el puntero de tortuga
hideturtle()
#Pen Up
up()
tracer(False)
#Lee el click en la pantalla con tap
onscreenclick(tap)
move()
#Main Lopp
done()
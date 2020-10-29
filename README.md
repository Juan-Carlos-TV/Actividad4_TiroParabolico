# Actividad 4:  Tiro Parabolico
## Herramientas computacionales: el arte de la programación

![](https://www.infojinaga.com.mx/wp-content/uploads/2017/01/Logo-Tec-de-Monterrey-e1484853084274.png)

### Descipción:
Como parte de las actividades a desarrollar durante esta semana tec, surge este proyecto que consiste en realizar modificaciones al juego de Cannon de Free Python Games [[aquí]](http://www.grantjenks.com/docs/freegames/cannon.html)
Estas modificaciones consisten en:
- La velocidad del movimiento para el proyectil y los balones sea más rápida
- Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.

### ¿Qué se utilizó para este proyecto?
Para realizar esta actividad se requirió de lo siguiente:
- Un IDE que permita trabajar con el lenguaje Python
- La paquetería de gráficos Turtle
- El paquete de freegames

### ¿Cómo se hizo?
#### Aumentar la velocidad del proyectil y los balones.
Para esta parte se tenían muchas opciones dependiendo del efecto que quisieramos conseguir. La escogida, en esta ocasión, fue la de aumentar el ontimer de la función move con el fin de aumentar la velocidad general del juego.
	ontimer(move, 10)

Sin embargo, también se podía modificar cada uno de manera independiente, cambiando, por un lado, el factor para obtener la velocidad en la función tap:

        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

Y cambiando la tasa de movimiento del balón:

	for target in targets:
        target.x -= 0.25

#### El juego nunca termina y reposiciona a los balones:
En esta parte lo que se hizo fue usar, en primer lugar, la función de "inside" dentro del código orginal con el fin de comprobar si el valon se ubicaba dentro de los límites de la pantalla:

	def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

Luego, se verifica que los elementos del arreglo de balones se encuentren dentro de la pantalla. Si alguno llega a salir su posición en x cambia a 200, es decir, el lado de derecho de la pantalla manteniendo la altura.

        for target in targets:
            if not inside(target):
                target.x = 200


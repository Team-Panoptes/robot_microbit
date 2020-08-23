from robot_microbit import Robot, Color
from microbit import sleep, pin1, display
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# faite en sorte que le robot tourne sur lui-même, par la gauche ou la droite, cela n'a pas d'importance.
# positionner le 3, 6 et un verre ou quelque chose de similaire en 9, 3.
# Quand il arrive en face du verre, il va en avant. Même avec 25 de vitesse la précision est pas folle
# donc il est possible qu'une fois le robot prêt à partir,
# si la distance n'est plus respectée, on donne un petit coup dans l'autre sens pour compenser (0.1 sec)
# lorsqu'il tourne pour "chercher le verre" , ses LED sont cyan (autrement, elles sont noire (éteinte)

while True:
    # your code here

    d = robot.distance_from_obstacle()

    if d > 50:
        robot.turn_left(25)
        robot.change_all_led_color(Color.cyan)
    else:
        if robot.distance_from_obstacle() > 50:
            robot.turn_right(25)
            sleep(100)
        robot.go_forward()
        robot.change_all_led_color(Color.black)
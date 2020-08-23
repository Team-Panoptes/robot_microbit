from robot_microbit import Robot, Color
from microbit import sleep, pin1, display
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# faite en sorte que le robot tourne sur lui-même, par la gauche ou la droite, cela n'a pas d'importance.
# positionner une boite en carton à moins de 30 cm de du robot
# Quand il arrive en face du verre, il doit s'arrêter (+- en face). (l'object est à moins de 50 cm).
# il est possible de jouer sur la vitesse pour rendre le robot plus précis (par exemple 25).


while True:
    # your code here

    d = robot.distance_from_obstacle()

    if d > 50:
        robot.turn_left(25)
    else:
        robot.stop()

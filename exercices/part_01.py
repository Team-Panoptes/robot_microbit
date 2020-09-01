# Exercice 1
# Objectif: Faire en sorte que le robot avance tout droit, et qu'il
# s'arrête quand il détecte du noir en dessous de lui.

from robot_microbit import *

robot.speed = 50

while True:
    if robot.on_ground():
        robot.go_forward()
    else:
        robot.stop()

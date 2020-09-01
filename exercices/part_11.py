# Exercice 11
# Objectif: Le robot suit le contour d'un dessin au sol (ex: Space Invader).

from robot_microbit import Robot, Color
from microbit import sleep, pin1
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# faite en sorte que le robot suive toujours le contour du dessin.

while True:
    # your code here

    if not robot.left_on_ground() and robot.right_on_ground():
        robot.go_forward()
    else:
        if not robot.right_on_ground():
            robot.turn_right()
        elif robot.left_on_ground():
            robot.turn_left()
# Exercice 7
# Objectif:  Quand le robot tourne à droite, la LED avant droite (index 3) est bleue. Quand
# il tourne à gauche, pareil pour la LED avant gauche (index 0).

from robot_microbit import *
from random import randint

robot.speed = 50

while True:
    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.go_backward()
        robot.change_all_led_color(Color.red)
        robot.wait(0.5)
        if randint(0, 1) == 1:
            robot.turn_right()
            robot.change_led_color(3, Color.blue)
        else:
            robot.turn_left()
            robot.change_led_color(0, Color.blue)
        robot.wait(0.5)
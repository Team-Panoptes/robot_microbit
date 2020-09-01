# Exercice 5
# Objectif: Cette fois, le robot va tourner au hasard vers le droite ou la gauche quand il
# rencontre du noir.

from robot_microbit import *
from random import randint

robot.speed = 50

while True:
    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        if randint(0, 1) == 1:
            robot.turn_right()
        else:
            robot.turn_left()
        robot.change_all_led_color(Color.red)
        robot.wait(0.5)

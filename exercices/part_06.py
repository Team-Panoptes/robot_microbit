# Exercice 6
# Objectif: Quand le robot rencontre du noir, il va reculer 0.5 secondes avant de tourner
# dans une direction aléatoire.

from robot_microbit import *
from random import randint

robot.speed = 50

while True:
    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.go_backward()
        robot.wait(0.5)
        if randint(0, 1) == 1:
            robot.turn_right()
        else:
            robot.turn_left()
        robot.change_all_led_color(Color.red)
        robot.wait(0.5)

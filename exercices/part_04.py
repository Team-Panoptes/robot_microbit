# Exercice 3
# Objectif: Quand le robot rencontre du noir, il ne va tourner que pendant une
# demi seconde avant d'essayer d'avancer. (Ne rien changer au reste.)

from robot_microbit import *

robot.speed = 50

while True:
    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.turn_right()
        robot.change_all_led_color(Color.red)
        robot.wait(0.5)

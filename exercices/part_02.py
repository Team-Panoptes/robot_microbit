# Exercice 2
# Objectif: Le même que pour l'exercice 1, mais quand le robot avance, les LEDs
# du dessous sont vertes, et rouges quand le robot est à l'arrêt.

from robot_microbit import *

robot.speed = 50

while True:
    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.stop()
        robot.change_all_led_color(Color.red)

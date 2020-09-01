# Exercice 3
# Objectif:  Maintenant, lorsque le robot rencontre un sol noir, au lieu de s'arrêter
# il va tourner à droite jusqu'à pouvoir de nouveau avancer.

from robot_microbit import *

robot.speed = 50

while True:
    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.turn_right()
        robot.change_all_led_color(Color.red)

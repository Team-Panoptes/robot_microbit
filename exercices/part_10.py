# Exercice 10
# Objectif: Le robot s'arrête et ses LEDs deviennent jaunes quand il est à moins de 5cm de sa cible.

from robot_microbit import *

robot.speed = 50

while True:
    distance = robot.distance_from_obstacle()

    if distance < 5:
        robot.stop()
        robot.change_all_led_color(Color.yellow)
    else:
        if distance > 50:
            robot.turn_left(25)
            robot.change_all_led_color(Color.cyan)
        else:
            if robot.distance_from_obstacle() > 50:
                robot.turn_right(25)
                robot.wait(0.1)
            robot.go_forward()
            robot.change_all_led_color(Color.black)
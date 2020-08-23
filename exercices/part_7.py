from robot_microbit import Robot, Color
from microbit import sleep, pin1
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# Garder le même exercice, mais lorsque le robot tourne à droite faite en sorte que la led avant droite (index=3)
# soit bleu. Faite de même quand le robot tourne à gauche (avec la led en index 0). Quand le robot recule il continue à afficher du rouge.

while True:
    # your code here


    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.go_backward()
        robot.change_all_led_color(Color.red)
        sleep(500)

        rnd = randint(0, 1)
        if rnd == 1:
            robot.turn_right()
            robot.change_led_color(3, Color.blue)
        else:
            robot.turn_left()
            robot.change_led_color(0, Color.blue)
        sleep(500)
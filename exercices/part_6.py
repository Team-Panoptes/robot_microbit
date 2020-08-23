from robot_microbit import Robot, Color
from microbit import sleep, pin1
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# Garder le même exercices sauf que le robot, lorsqu'il rencontre du noir,
# fait un léger mouvement en arrière (0.5 sec) avant de tourné (toujours de manière aléatoire)
while True:
    # your code here


    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.go_backward()
        sleep(500)
        rnd = randint(0, 1)
        if rnd == 1:
            robot.turn_right()
        else:
            robot.turn_left()
        robot.change_all_led_color(Color.red)
        sleep(500)
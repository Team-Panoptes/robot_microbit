from robot_microbit import Robot, Color
from microbit import sleep, pin1, display
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# faite en sorte que le robot s'arrête quand il est à moins de 5 de sa cible. Quand il a trouvé sa cible la couleur devient jaune

while True:
    # your code here

    d = robot.distance_from_obstacle()

    if d < 5:
        robot.stop()
        robot.change_all_led_color(Color.yellow)
    else:
        if d > 50:
            robot.turn_left(25)
            robot.change_all_led_color(Color.cyan)
        else:
            if robot.distance_from_obstacle() > 50:
                robot.turn_right(25)
                sleep(100)
            robot.go_forward()
            robot.change_all_led_color(Color.black)
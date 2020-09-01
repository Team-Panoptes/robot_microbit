from robot_microbit import Robot, Color
from microbit import sleep, pin1
from random import randint

robot = Robot()
robot.speed = 100
robot.beep(2)
while True:
    robot.change_all_led_color(Color.green)
    if robot.distance_from_obstacle() <= 10:
        robot.change_all_led_color(Color.red)
        if randint(0,1) == 1:
            robot.turn_left()
        else:
            robot.turn_right()
        sleep(randint(1000,2000))
    else:
        robot.go_forward()


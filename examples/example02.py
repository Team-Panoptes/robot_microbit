from robot_microbit import Robot, Color
from microbit import sleep, pin1
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 100
robot.beep(2)
distance =0

while True:
    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
        if robot.distance_from_obstacle() <= 10:
            robot.change_all_led_color(Color.red)
            robot.go_backward()
            sleep(500)
            robot.search_escape()
    else:
        robot.stop()
        robot.change_all_led_color(Color.cyan)
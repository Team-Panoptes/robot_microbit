from robot_microbit import Robot, Color
from microbit import sleep, pin1
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# Même chose que le premier, mais quand le robot roule les LED sont vertes quand
# il s'arrête elles deviennent rouge.

while True:
    # your code here


    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.stop()
        robot.change_all_led_color(Color.red)
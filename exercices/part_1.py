from robot_microbit import Robot, Color
from microbit import sleep, pin1
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# but de l'exercice: faire en sorte que le robot aie tout droit.
# et que lorsqu'il rencontre du noir en dessous de lui, il s'arrête.

while True:
    # your code here

    if robot.on_ground():
        robot.go_forward()
    else:
        robot.stop()
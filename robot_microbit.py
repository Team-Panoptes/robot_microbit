from microbit import *
from machine import time_pulse_us
from neopixel import NeoPixel
from time import sleep_ms, ticks_diff, ticks_ms
import music
from math import sqrt

class Color:
    cyan = 0, 255, 255
    red = 255, 0, 0
    blue = 0, 0, 255
    yellow = 255, 255, 0
    purple = 255, 0, 255
    green = 0, 255, 0
    white = 255, 255, 255
    black = 0, 0, 0


class Robot:
    def __init__(self, address=0x10):
        self.speed = 10
        self.address = address

    def change_led_color(self, index, rgb, number=1, entry_point=pin15):
        np = NeoPixel(entry_point, 4)

        if isinstance(rgb, list):
            colors = rgb
        else:
            colors = [rgb] * number

        for i, color in enumerate(colors):
            np[(index + i) % 4] = color
        np.show()

    def change_all_led_color(self, rgb):
        self.change_led_color(0, rgb, 4)


    def engine(self, index, speed=None):
        if speed is None:
            speed = self.speed
        sens = 0 if speed >= 0 else 1
        speed = abs(speed)*255//100
        try:
            i2c.write(self.address, bytearray([index, sens, speed]))
        except:
            pass

    def engine_right(self, speed=None):
        self.engine(index=2, speed=speed)

    def engine_left(self, speed=None):
        self.engine(index=0, speed=speed)

    def go_forward(self, speed=None):
        self.engine_right(speed)
        self.engine_left(speed)

    def go_backward(self, speed=None):
        if speed is None:
            speed = self.speed

        self.go_forward(-speed)

    def turn_right(self, speed=None):
        if speed is None:
            speed = self.speed

        self.engine_left(speed)
        self.engine_right(-speed)

    def turn_left(self, speed=None):
        if speed is None:
            speed = self.speed

        self.engine_right(speed)
        self.engine_left(-speed)

    def stop(self):
        self.engine_left(speed=0)
        self.engine_right(speed=0)

    def wait(self, seconds):
        """
        Makes the robot stop for a given amount of seconds. Translates seconds into milliseconds.
        """
        sleep(seconds * 1000)

    def beep(self, number=1):
        tune = ["D6:1", "R:1"]
        tunes = []
        for n in range(number):
            tunes += tune
        music.play(tunes)

    def distance_from_obstacle(self):
        pin1.write_digital(1)
        sleep_ms(10)
        pin1.write_digital(0)
        pin2.read_digital()

        t = time_pulse_us(pin2, 1)
        distance = 340 * t / 20000
        return distance

    def search_escape(self):
        distance =0
        search_speed = int(self.speed * 0.15)
        start = ticks_ms()
        turn = True
        self.turn_right(search_speed)
        while turn:
            distance = max(distance, self.distance_from_obstacle())

            if ticks_diff(ticks_ms(), start) >= 50 * self.speed:
                turn = False
                self.stop()

            distance -= 1

        turn = True
        self.turn_left(search_speed)
        while turn:
            if self.distance_from_obstacle() >= distance:
                self.stop()
                turn = False

        return

    def on_ground(self):
        """
        Returns True if p13 or p14 return 1
        That means that there is a ground (non-black) bellow the robot.
        """

        return  min(self.ground_status()) == 1

    def left_on_ground(self):
        """
        Returns True if p13 return 1
        That means that there is a ground (non-black) bellow left part of the robot the robot.
        """

        return self.ground_status()[0] == 1

    def right_on_ground(self):
        """
        Returns True if p14 return 1
        That means that there is a ground (non-black) bellow right part of the robot the robot.
        """

        return self.ground_status()[1] == 1

    def ground_status(self):
        """
        Returns a tuple with the state on p13 and p14.

        """

        return pin13.read_digital(),  pin14.read_digital()

robot = Robot()
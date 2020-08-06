from microbit import i2c, pin1, pin2, pin13, pin14, pin15, accelerometer
from machine import time_pulse_us
from neopixel import NeoPixel
from time import sleep_ms, ticks_diff, ticks_ms
import music
from math import sqrt

class Color:
    cyan = 0, 255, 255
    red = 255, 0, 0
    blue = 0, 255, 0
    yellow = 0, 255, 255
    purple = 255, 0, 255
    green = 0, 255, 0
    withe = 255, 255, 255
    black = 0, 0, 0


class Robot:
    def __init__(self, addresse=0x10):
        self.speed = 10
        self.addresse = addresse

    def change_led_color(self, rgb, entry_point=pin15, number=1):
        np = NeoPixel(entry_point, number)

        for index in range(number):
            np[index] = rgb
        np.show()

    def change_all_led_color(self, rgb):
        self.change_led_color(rgb, number=4)

    def engine(self, index, speed=None):
        if speed is None:
            speed = self.speed
        sens = 0 if speed >= 0 else 1
        speed = abs(speed)*255//100
        i2c.write(self.addresse, bytearray([index, sens, speed]))

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

    def turn_left(self, speed=None):
        if speed is None:
            speed = self.speed

        self.engine_left(speed)
        self.engine_right(-speed)

    def turn_right(self, speed=None):
        if speed is None:
            speed = self.speed

        self.engine_right(speed)
        self.engine_left(-speed)

    def stop(self):
        self.engine_left(speed=0)
        self.engine_right(speed=0)

    def bip(self, number=1):
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

        return pin14.read_digital() == 1 or pin13.read_digital() == 1
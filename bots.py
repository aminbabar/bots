"""
 *****************************************************************************
   FILE:  bots.py

   AUTHOR: Amin Babar

   ASSIGNMENT: bots

   DATE: 12/13/2017

   DESCRIPTION:This program creates 2 bots which when clicked on move randomly.
   When the bots crash they turn red and when they uncrash they turn yellow.

 *****************************************************************************
"""
# CITE: Asked for help from Alex Chalk, Mahdi Mahil abd Sofia Maeztu with
# the move function and the overlap function.

from cs110graphics import *

import random


class Bot(object):
    def __init__(self, win, width, center, direction='east', speed=20):
        self._win = win
        self._width = width
        self._center = center
        self._direction = direction
        self._speed = speed
        self._body = Square(win, width, center)
        self._body.set_fill_color("yellow")
        self._parts = [self._body]

    # adds the bot to the window
    def add_to_window(self):
        self._win.add(self._body)

    # makes the bots clickable
    def add_handler(self, handler):
        for part in self._parts:
            part.add_handler(handler)

    # moves the bot in the direction it faces with self._speed
    def move(self):
        if self._direction == "north":
            for part in self._parts:
                part.move(0, - self._speed)
            self._center = (self._center[0], self._center[1] - self._speed)
        elif self._direction == "south":
            for part in self._parts:
                part.move(0, self._speed)
            self._center = (self._center[0], self._center[1] + self._speed)
        elif self._direction == "east":
            for part in self._parts:
                part.move(self._speed, 0)
            self._center = (self._center[0] + self._speed, self._center[1])
        else:
            for part in self._parts:
                part.move(- self._speed, 0)
            self._center = (self._center[0] - self._speed, self._center[1])

    # changes the orientation of bot towards left
    def turn_left(self):
        if self._direction == "north":
            self._direction = "west"
        elif self._direction == "west":
            self._direction = "south"
        elif self._direction == "south":
            self._direction = "east"
        else:
            self._direction = "north"

    # changes the orientation of the bot towards right
    def turn_right(self):
        if self._direction == "north":
            self._direction = "east"
        elif self._direction == "east":
            self._direction = "south"
        elif self._direction == "south":
            self._direction = "west"
        else:
            self._direction = "north"

    # increases the speed of the bot
    def speed_up(self):
        self._speed += 50

    # decreases the speed of the bot
    def slow_down(self):
        self._speed -= 50

    # decides what happens when the bots crash
    def crash(self):
        self._body.set_fill_color("red")

    # decides what happens when the bots uncrash
    def uncrash(self):
        self._body.set_fill_color("yellow")

    # gets the width of the bot
    def get_width(self):
        return self._witdh

    # returns the center of the bot
    def get_center(self):
        return self._center

    # determines when the crash occurs based on the distance vertical and
    # horizontal distances from the center of the 2 bots
    def overlaps(self, bot2):
        diff_x = (abs(self._center[0] - bot2._center[0]))
        diff_y = (abs(self._center[1] - bot2._center[1]))
        distance_center = self.get_width() / 2 + other.get_width() / 2

        if diff_x < distance_center and diff_y < distance_center:
            return True

        return False


class BotHandler(EventHandler):
    def __init__(self, bot):
        EventHandler.__init__(self)
        self._bot = bot

    # random actions that take place when the bots are clicked
    def handle_mouse_release(self, event):
        num = random.randint(0, 3)
        if num == 0:
            self._bot.move()
        elif num == 1:
            self._bot.turn_left()
        else:
            self._bot.turn_right()


def program(win):
    bot = Bot(win, 100, (200, 200))
    bot.add_to_window()
    bot.add_handler(BotHandler(bot))

    bot_2 = Bot(win, 150, (400, 200))
    bot_2.add_to_window()
    bot.add_handler(BotHandler(bot_2))


def main():
    StartGraphicsSystem(program)


if __name__ == "__main__":
    main()

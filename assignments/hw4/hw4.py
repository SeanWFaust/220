"""
Name: Sean Faust
HW4.py

Problem: This homework goes over the different functions and uses of the graphics library
    and how to use them in different creative ways.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks + 1):
        center = win.getMouse()
        sEcornerx = center.getX() - 25
        sEcornery = center.getY() - 25
        nWcornerx = center.getX() + 25
        nWcornery = center.getY() + 25
        shape = Rectangle(Point(sEcornerx, sEcornery), Point(nWcornerx, nWcornery))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    close_pt = Point(width / 2, height - 100)
    instructions = Text(close_pt, "Click to Close")
    instructions.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    pass


def circle():
    pass


def pi2():
    pass


if __name__ == '__main__':
    pass

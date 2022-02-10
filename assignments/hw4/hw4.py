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
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)
    click1 = win.getMouse()
    click2 = win.getMouse()
    rec = Rectangle(Point(click1.getX(), click1.getY()), Point(click2.getX(), click2.getY()))
    rec.setOutline("Green")
    rec.setFill("Green")
    rec.draw(win)
    length = (400 - click1.getX()) - (400 - click2.getX())
    hei = (400 - click1.getY()) - (400 - click2.getY())
    perimeter = (length * 2) + (hei * 2)
    perimeter_pt = Point(200, 20)
    perimeter_text = Text(perimeter_pt, "Perimeter: ")
    perimeter_text.draw(win)
    area = (length * hei)
    area_text_pt = Point(200, 40)
    area_text = Text(area_text_pt, "Area:")
    area_text.draw(win)
    area_pt = Point(250, 40)
    area_num = Text(area_pt, area)
    area_num.draw(win)
    perm_num_pt = Point(260, 20)
    perm_num = Text(perm_num_pt, perimeter)
    perm_num.draw(win)
    close_pt = Point(200, 200)
    close_text = Text(close_pt, "Click again to close")
    close_text.draw(win)
    win.getMouse()
    win.close()

def circle():
    pass


def pi2():
    pass


if __name__ == '__main__':
    pass

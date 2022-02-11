"""
Name: Sean Faust
HW4.py

Problem: This homework goes over the different functions and uses of the graphics library
    and how to use them in different creative ways.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to make a square")
    instructions.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks + 1):
        center = win.getMouse()
        clickx1 = center.getX() - 25
        clicky1 = center.getY() - 25
        clickx2 = center.getX() + 25
        clicky2 = center.getY() + 25
        shape = Rectangle(Point(clickx1, clicky1), Point(clickx2, clicky2))
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
    perimeter_text = Text(Point(200, 20), "Perimeter: ")
    perimeter_text.draw(win)
    area = (length * hei)
    area_text = Text(Point(200, 40), "Area:")
    area_text.draw(win)
    area_num = Text(Point(250, 40), area)
    area_num.draw(win)
    perm_num = Text(Point(260, 20), perimeter)
    perm_num.draw(win)
    close_text = Text(Point(200, 200), "Click again to close")
    close_text.draw(win)
    win.getMouse()
    win.close()

def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)
    click1 = win.getMouse()
    click2 = win.getMouse()
    x_val = (click2.getX() - click1.getX()) ** 2
    y_val = (click2.getY() - click1.getY()) ** 2
    radius = math.sqrt((x_val + y_val))
    circle = Circle(click1, radius)
    circle.setFill("Blue")
    circle.setOutline(("Black"))
    circle.draw(win)
    radius_txt = Text(Point(200, 20), "Radius:")
    radius_txt.draw(win)
    radius_num = Text(Point(200, 40), radius)
    radius_num.draw(win)
    close_pt = Point(200, 200)
    close_text = Text(close_pt, "Click again to close")
    close_text.draw(win)
    win.getMouse()
    win.close()


def pi2():
    near_pi = 0
    numer = 4
    denom = 1
    iterations = eval(input("Enter the number of terms to sum:"))
    for i in range(1, iterations + 1):
        near_pi += (numer / denom)
        denom += 2
        numer *= -1
    print("pi approximation: ", near_pi)
    print("accuracy: ", near_pi - math.pi)



if __name__ == '__main__':
    pass

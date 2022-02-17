"""
Name: Sean Faust
Lab5.py

Problem: This lab has us using more of the graphics library and processing through different
strings.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math

def triangle():
    height = 400
    width = 400
    win = GraphWin("Triangle", width, height)
    instructions = Text(Point(200, 50), "Click 3 times to make a triangle.")
    instructions.draw(win)
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    tri = Polygon(Point(point1.getX(), point1.getY()), Point(point2.getX(), point2.getY()),
                  Point(point3.getX(), point3.getY()))
    tri.draw(win)
    tri.setFill("Black")
    lside1 = math.sqrt((((point2.getX() - point1.getX())) ** 2) + ((point2.getY() - point1.getY()) ** 2))
    lside2 = math.sqrt((((point3.getX() - point2.getX())) ** 2) + ((point3.getY() - point2.getY()) ** 2))
    lside3 = math.sqrt((((point3.getX() - point1.getX())) ** 2) + ((point3.getY() - point1.getY()) ** 2))
    perimeter = lside1 + lside2 + lside3
    perimtext = Text(Point(200, 75), "The perimeter of your triangle is " + str(round(perimeter, 2)))
    perimtext.draw(win)
    variable = (lside1 + lside2 + lside3) / 2
    area = math.sqrt(variable * (variable - lside1) * (variable - lside2) * (variable - lside3))
    areatxt = Text(Point(200, 100), "The Area of your triangle is " + str(round(area, 2)))
    areatxt.draw(win)
    close = Text(Point(200, 350), "Click to Close")
    close.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    red_entry.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_entry.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_entry.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    win.getMouse()

    for i in range(5):
        win.getMouse()
        shape.setFill(color_rgb(int(red_entry.getText()), int(green_entry.getText()),
                                int(blue_entry.getText())))

    close = Text(Point(200, 350), "Click to Close")
    close.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    message = input("Enter a string:")
    print("1: ", message[0])
    print("2: ", message[-1])
    print("3: ", str(message[2:6]))
    print("4: ", str(message[0]) + str(message[-1]))
    print("5: ", str(message[0:3]) * 3)
    print("6: ", end=' ')
    for i in message:
        print(i)
    print(len(message))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print(values[1] + values[3])
    print(values[0] + values[2])
    print(values[2:5])
    values2 = [values[2], values[3], values[0]]
    print(values2)
    values3 = [values[2], values[0], float(values[5])]
    print(values3)
    print(values[0] + values[2] + float(values[5]))
    print(len(values))


def another_series():
    total = 0
    entry = eval(input("How many terms do you want?"))
    for i in range(entry):
        seq = ((i % 3) + 1) * 2
        print(seq, end=' ')
        total += seq
    print()
    print("Your total is: ", total)


def target():
    length = 400
    width = 400
    win = GraphWin("Target", width, length)
    win.setBackground("Black")
    circleW = Circle(Point(200, 200), 200)
    circleW.draw(win)
    circleW.setFill("White")
    circleBk = Circle(Point(200, 200), 160)
    circleBk.draw(win)
    circleBk.setFill("Black")
    circleB = Circle(Point(200, 200), 120)
    circleB.draw(win)
    circleB.setFill("Blue")
    circleR = Circle(Point(200, 200), 80)
    circleR.draw(win)
    circleR.setFill("Red")
    circleY = Circle(Point(200, 200), 40)
    circleY.draw(win)
    circleY.setFill("Yellow")
    closetxt = Text(Point(200, 380), "Click to close")
    closetxt.draw(win)
    win.getMouse()
    win.close()

"""
Name: Sean Faust
Lab8.py

Problem: This lab had me make a program that generated two balls randomly in my window
and had them each bounce off the 4 walls, changing direction, and also bouncing off each other, which caused
them to reverse direction.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from ctypes.wintypes import RGB
from random import randint
from graphics import *
import math


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball, ball2):
    ball_center = ball.getCenter()
    ball2center = ball2.getCenter()
    x_difference = ((ball2center.getX() - ball_center.getX()) ** 2)
    y_difference = ((ball2center.getY() - ball_center.getY()) ** 2)
    distance = math.sqrt(x_difference + y_difference)
    total_radius = ball.getRadius() + ball2.getRadius()
    if distance <= total_radius:
        return True
    else:
        return False


def hit_vertical(ball, win):
    ball_radius = ball.getRadius()
    ball_center = ball.getCenter()
    topside = 0
    bottomside = win.getHeight()
    if ball_center.getY() + ball_radius >= bottomside:
        return True
    elif ball_center.getY() - ball_radius <= topside:
        return True
    else:
        return False


def hit_horizontal(ball, win):
    ball_radius = ball.getRadius()
    ball_center = ball.getCenter()
    leftside = 0
    rightside = win.getWidth()
    if ball_center.getX() + ball_radius >= rightside:
        return True
    elif ball_center.getX() - ball_radius <= leftside:
        return True
    else:
        return False


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return color_rgb(red, green, blue)


def bumper():
    width = 600
    height = 600
    win = GraphWin("Bumper Cars!", width, height)

    center1 = Point(randint(0, 600), randint(0, 600))
    center2 = Point(randint(0, 600), randint(0, 600))
    radius = 20
    circle1 = Circle(center1, radius)
    circle1.setFill(get_random_color())
    circle1.draw(win)
    circle2 = Circle(center2, radius)
    circle2.setFill(get_random_color())
    circle2.draw(win)
    speedC1X = get_random(10)
    speedC1Y = get_random(10)
    speedC2X = get_random(10)
    speedC2Y = get_random(10)
    while not win.checkMouse():
        circle1.move(speedC1X, speedC1Y)
        circle2.move(speedC2X, speedC2Y)
        if did_collide(circle1, circle2):
            speedC1X *= -1
            speedC1Y *= -1
            speedC2X *= -1
            speedC2Y *= -1
        if hit_vertical(circle1, win):
            speedC1Y *= -1
        if hit_vertical(circle2, win):
            speedC2Y *= -1
        if hit_horizontal(circle1, win):
            speedC1X *= -1
        if hit_horizontal(circle2, win):
            speedC2X *= -1
        time.sleep(.1)
    win.getMouse()
    win.close()


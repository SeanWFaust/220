"""
Name: Sean Faust
lAB10.py

Problem: This program has us making a door and a button on a screen with interactivity.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


class Door:

    def __init__(self, shape, text):
        self.shape = shape
        self.text = Text(shape.getCenter(), text)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        point1 = self.shape.getP1()
        point2 = self.shape.getP2()
        if point2.getX() >= point.getX() >= point1.getX() and point2.getY() >= point.getY() >= point1.getY():
            return True
        else:
            return False

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def is_secret(self):
        if self.secret == True:
            return True
        else:
            return False

    def set_secret(self, secret):
        self.secret = secret


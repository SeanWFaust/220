"""
Name: Sean Faust
lAB10.py

Problem: This program has us making a door and a button on a screen with interactivity.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, new_label):
        self.text.setText(new_label)

    def draw(self, win):
        self.text.draw(win)
        self.shape.draw(win)

    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, point):
        point1 = self.shape.getP1()
        point2 = self.shape.getP2()
        if point2.getX() >= point.getX() >= point1.getX() and point2.getY() >= point.getY() >= point1.getY():
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)


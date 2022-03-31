"""
Name: Sean Faust
lAB10.py

Problem: This program has us making a door and a button on a screen with interactivity.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from button import Button
from door import Door
from graphics import *

def main():
    width = 400
    height = 400
    win = GraphWin('button game', width, height)
    exit = Button(Rectangle(Point(100, 100), Point(300, 150)), 'Exit')
    exit.draw(win)
    door = Door(Rectangle(Point(100, 200), Point(300, 475)), 'Closed')
    door.draw(win)
    i = 1
    while i < 2:
        i = 1
        while i == 1:
            if door.is_clicked(win.getMouse()):
                door.open('red', 'Open')
                i = 0
            elif exit.is_clicked(win.getMouse()):
                i = 3
        while i == 0:
            if door.is_clicked(win.getMouse()):
                door.close('white', 'closed')
                i = 1
            elif exit.is_clicked(win.getMouse()):
                i = 3
    win.close()

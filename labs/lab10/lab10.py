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
    door = Door(Rectangle(Point(100, 200), Point(300, 375)), 'Closed')
    door.draw(win)
    door.close('white', 'Closed')
    while not door.is_secret():
        if door.is_clicked(win.getMouse()) and door.close('white', 'Closed'):
            door.open('red', 'Open')
        if door.is_clicked(win.getMouse()) and door.open('red', 'Open'):
            door.close('white', 'Closed')
        elif exit.is_clicked(win.getMouse()):
            door.set_secret(True)
    win.close()

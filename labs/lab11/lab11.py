"""
Name: Sean Faust
Lab1.py

Problem: This lab has me using my previously made Classes to make a "Three Door Game".

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from lab10.button import Button
from lab10.door import Door
from random import randint
from graphics import *


def three_door_game():
    width = 600
    height = 600
    win = GraphWin("Three Door Game", width, height)
    winningbox = Rectangle(Point(5, 25), Point(55, 75))
    losingbox = Rectangle(Point(55, 25), Point(105, 75))
    winningbox.draw(win)
    losingbox.draw(win)
    winstext = Text(Point(30, 15), "Wins")
    winstext.draw(win)
    losestext = Text(Point(80, 15), "Loses")
    losestext.draw(win)
    exitbutton = Button(Rectangle(Point(495, 25), Point(570, 75)), "Exit")
    exitbutton.draw(win)
    door1 = Door(Rectangle(Point(50, 200), Point(150, 500)), "Door 1")
    door1.close("grey", "Door 1")
    door1.draw(win)
    door2 = Door(Rectangle(Point(250, 200), Point(350, 500)), "Door 2")
    door2.draw(win)
    door2.close("grey", "Door 2")
    door3 = Door(Rectangle(Point(450, 200), Point(550, 500)), "Door 3")
    door3.draw(win)
    door3.close("grey", "Door 3")
    gamewintext = Text(Point(300, 150), "You guessed the correct door!")
    gamelosttext = Text(Point(300, 150), "You did not guess the correct door.")
    playagaintext = Text(Point(300, 550), "Click anywhere to play again.")
    win_acc = 0
    lose_acc = 0
    door_list = [door1, door2, door3]
    click = win.getMouse()
    while not exitbutton.is_clicked(click):
        win_door = randint(1, 3)
        win_num = Text(Point(30, 50), win_acc)
        win_num.draw(win)
        lose_num = Text(Point(80, 50), lose_acc)
        lose_num.draw(win)
        if door1.is_clicked(click) and win_door == 1:
            win_acc += 1
            gamewintext.draw(win)
            playagaintext.draw(win)
            door1.open("green", "Door 1")
        elif door2.is_clicked(click) and win_door == 2:
            win_acc += 1
            gamewintext.draw(win)
            playagaintext.draw(win)
            door2.open("green", "Door 2")
        elif door3.is_clicked(click) and win_door == 3:
            win_acc += 1
            gamewintext.draw(win)
            playagaintext.draw(win)
            door3.close("green", "Door 3")
        else:
            if door1.is_clicked(click) and win_door != 1:
                door1.open("red", "Door 1")
                door_list[win_door - 1].open("green", "Door {}".format(win_door))
                lose_acc += 1
                gamelosttext.draw(win)
                playagaintext.draw(win)
            elif door2.is_clicked(click) and win_door != 2:
                door2.open("red", "Door 2")
                door_list[win_door - 1].open("green", "Door {}".format(win_door))
                lose_acc += 1
                gamelosttext.draw(win)
                playagaintext.draw(win)
            elif door3.is_clicked(click) and win_door != 3:
                door3.open("red", "Door 3")
                door_list[win_door - 1].open("green", "Door {}".format(win_door))
                lose_acc += 1
                gamelosttext.draw(win)
                playagaintext.draw(win)
        click = win.getMouse()
        win_num.undraw()
        lose_num.undraw()
        gamewintext.undraw()
        gamelosttext.undraw()
        playagaintext.undraw()
        door1.close("grey", "Door 1")
        door2.close("grey", "Door 2")
        door3.close("grey", "Door 3")
    win.close()

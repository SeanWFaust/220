"""
Name: Sean Faust
Lab2.py

Problem: This program is to take a random amount of inputs from the user and
    output the Root-Square-Mean, Harmonic Mean, and the Geometric Mean to the User.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def means():
    amounts_RMS = 0
    amounts_HM = 0
    amounts_GM = 1
    loop_amount = eval(input("How many values do you want to enter? "))
    for i in range(loop_amount):
        amounts = (eval(input("Enter amount: ")))
        amounts_RMS += amounts ** 2
        amounts_HM += (1 / amounts)
        amounts_GM *= amounts
    print("The Root-Mean-Square(RMS) is: ", round(math.sqrt(amounts_RMS / loop_amount), 3))
    print("The Harmonic Mean is: ", round(loop_amount / amounts_HM, 1))
    print("The Geometric Mean is: ", round((amounts_GM ** (1 / loop_amount)), 3))
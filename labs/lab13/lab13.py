"""
Name: Sean Faust
Lab13.py

Problem: This had me searching a file for a number over 830 or exactly 500 and giving a
warning or alert, respectively, to the user along with a timestamp of when the number appeared.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    file = open(filename, 'r')
    file_list = file.read()
    file.close()
    file_list = file_list.split(' ')
    incr = 0
    while incr < len(file_list):
        if eval(file_list[incr]) > 830:
            print('Warning trade over 830 happened at ' + str(incr + 1))
        elif eval(file_list[incr]) == 500:
            print('Alert! Exactly 500 trades at timestamp ' + str(incr + 1))
        incr += 1

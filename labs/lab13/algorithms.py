from graphics import *

"""
Name: Sean Faust
Lab13.py

Problem: In this lab I had to write a program to do a selection sort on a list, a program to calculate
the area of a rectangle based on a Rectangle object, and a program to sort a list of Rectangle objects based
on their area using the previous function.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    incr = 0
    numbered_list = []
    data = open(filename, 'r').read()
    data = data.replace('\n', ' ')
    data = list(data.split(' '))
    while incr < len(data):
        numbered_list.append(eval(data[incr]))
        incr += 1
    numbered_list.sort()
    return numbered_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return i
        else:
            i += 1
    return -1


def calc_area(rect):
    point1 = rect.getP1()
    point2 = rect.getP2()
    lowx_val = point1.getX()
    lowy_val = point1.getY()
    highx_val = point2.getX()
    highy_val = point2.getY()
    height = abs(highy_val - lowy_val)
    width = abs(highx_val - lowx_val)
    return height * width


def selection_sort(values):
    for num in range(len(values)):
        min_loc = num # get the number to potentially replace
        for num_after in range(num + 1, len(values)): # loop through the numbers after min_loc
            if values[num_after] < values[min_loc]:
                min_loc = num_after # if found a number that was less than min_loc set min loc to that number.
        values[num], values[min_loc] = values[min_loc], values[num] # once through the rest of the list,
                                                                    # swap positions for the two numbers


def rect_sort(rectangles):
    for rect in range(len(rectangles)):
        min_loc = rect # I used the same function as above I just calc'd the area of the rectangles
        for search_rect in range(rect + 1, len(rectangles)):# and used them to search through the list.
            if calc_area(rectangles[search_rect]) < calc_area(rectangles[min_loc]):
                min_loc = search_rect
        rectangles[rect], rectangles[min_loc] = rectangles[min_loc], rectangles[rect]

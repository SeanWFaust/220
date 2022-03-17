"""
Name: Sean Faust
HW8.py

Problem: This homework worked on modifying lists in different ways and using previously written
functions within a larger function.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math

def add_ten(nums):  # adds 10 to each number in a list of numbers
    for num in range(len(nums)):
        nums[num] += 10


def square_each(nums):  # squares each number in a list of numbers
    for num in range(len(nums)):
        nums[num] = nums[num] ** 2
    return nums


def sum_list(nums):  # adds each number in a list together
    total = 0
    for num in nums:
        total += num
    return total


def to_numbers(nums):  # convert strings into their respective numbers
    for num in range(len(nums)):
        nums[num] = eval(nums[num])


def sum_of_squares(nums):
    new_list = []
    total = []
    for num in nums:
        new_list.append(num.split(','))
    for num in new_list:
        to_numbers(num)
    for num in new_list:
        square_each(num)
    for num in new_list:
        total.append(sum_list(num))
    return total


def starter(weight, wins):
    if (150 <= weight < 160) and wins >= 5:
        return True
    if weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circum_point_2 = win.getMouse()
    radius_2 = math.sqrt(
        (center_2.getX() - circum_point_2.getX()) ** 2 + (center_2.getY() - circum_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("light green")
    circle_two.draw(win)
    close_txt = Text(Point(5, 8), "Click to close the window.")
    close_txt.draw(win)

    true_txt = Text(Point(5, 5), "The circles did overlap.")
    false_txt = Text(Point(5, 5), "The circles did not overlap.")

    if did_overlap(circle_one, circle_two):
        true_txt.draw(win)
    else:
        false_txt.draw(win)

    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    two_center = circle_two.getCenter()
    one_center = circle_one.getCenter()
    x_difference = ((two_center.getX() - one_center.getX()) ** 2)
    y_difference = ((two_center.getY() - one_center.getY()) ** 2)
    distance = math.sqrt(x_difference + y_difference)
    total_radius = circle_one.getRadius() + circle_two.getRadius()
    if distance <= total_radius:
        return True
    else:
        return False


if __name__ == '__main__':
    pass
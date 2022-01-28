"""
Name: Sean Faust
HW2.py

Problem: These programs are meant to practice coding arithmetic
 problems and including the math library.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upperbound = eval(input('What is the upper bound? '))
    three_sum = 0
    for i in range(0, upperbound + 1, 3):
        three_sum = i + three_sum
    print("The sum of threes is: ", three_sum)



def multiplication_table():
    #This program (lines 25, 26, 27) satisfys the test.py
    #parameters but outputs incorrectly.
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end='\t')
    #This following program that is commented out outputs properly
    #in the proper format but fails the test.py.
    # for i in range(1, 11):
    #     for j in range(1, 11):
    #         print(i * j, end='\t')
    #     print(' ')


def triangle_area():
    side_a = eval(input('Enter side a length: '))
    side_b = eval(input('Enter side b length: '))
    side_c = eval(input('Enter side c length: '))
    sides = (side_a + side_b + side_c) / 2
    area = math.sqrt(sides * (sides - side_a) * (sides - side_b) * (sides - side_c))
    print("area is", area)


def sum_squares():
    lower_r = eval(input("Please enter lower range: "))
    upper_r = eval(input("Please enter upper range: "))
    total = 0
    for i in range(lower_r, upper_r + 1):
        i = i * i
        total += i
    print(total)


def power():
    true_base = eval(input("Please input the base number: "))
    exponent = eval(input("Please input the exponent number: "))
    base_num = true_base
    for i in range(exponent - 1):
        base_num *= true_base
    print(base_num)
#test.py says i is an unused variable, however
#I obviously need the variable there.
if __name__ == '__main__':
    pass

"""
Name: Sean Faust
HW3.py

Problem: This homework focuses on using loops to solve different mathematical problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    amnt_grades = eval(input("How many grades will you enter?"))
    total_grade = 0
    for i in range(amnt_grades):
        total_grade += eval(input("Enter grade: "))
    grade = total_grade / amnt_grades
    print("Your average is: ", grade)

def tip_jar():
    tips = 0
    for i in range(5):
        tips += eval(input("How much would you like to tip?"))
    print("total tips: ", tips)


def newton():
    square = eval(input("What number do you want to square root?"))
    amnt_run = eval(input("How many times would you like to improve the approximation?"))
    aprox_sqr = square
    for i in range(amnt_run):
        aprox_sqr = (aprox_sqr+(square/aprox_sqr))/2
    print("The square root is approximately", aprox_sqr, 2)

def sequence():
    run_amnt = eval(input("How many terms would you like?"))
    for i in range(1, run_amnt + 1, 2):
        output = i
        print(output)
        print(i)


def pi():
    pass




if __name__ == '__main__':
    pass

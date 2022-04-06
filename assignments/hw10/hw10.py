"""
Name: Sean Faust
HW10.py

Problem: This homework has me going through different functions with while loops
to perform different functions and also modifying or creating different classes.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def fibonacci(number):
    sequence = []
    incr = 1
    start = 1
    additive_num = 0
    while incr <= number:
        sequence.append(start)
        start += additive_num
        additive_num = sequence[-1]
        incr += 1
    return sequence[-1]

def double_investment(principle, rate):
    original = principle
    something = False
    count = 0
    while not something:
        total = principle * (1 + rate)
        count += 1
        if total >= (2 * original):
            something = True
        else:
            principle = total
    return count

def syracuse(number):
    sequence = []
    sequence.append(int(number))
    while number != 1:
        if number % 2 == 0:
            number /= 2
            sequence.append(int(number))
        elif number % 2 == 1:
            number = (3 * number) + 1
            sequence.append(int(number))
    return sequence


def goldbach(number):
    count = 2
    if number % 2 != 0:
        return None
    while count < number:
        if is_prime(count):
            second_prime = number - count
            if is_prime(second_prime):
                return count, second_prime
            else:
                count += 1
        else:
            count += 1

def is_prime(number):
    count = 2
    while count < number:
        prime = number % count
        if prime == 0:
            return False
        else:
            count += 1
    return True

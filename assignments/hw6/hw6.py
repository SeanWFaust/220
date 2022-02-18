"""
Name: Sean Faust
HW6.py

Problem: Working with strings
Writing functions that accept arguments and return values.
Modifying an object in a parameter


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def cash_converter():
    number = input("Enter an integer:")
    print("That is ${:,.2f}".format(float(number)))


def encode():
    message = input("Enter a message:")
    key = input("Enter a key:")
    output = ''
    for letter in message:
        output += chr(ord(letter) + int(key))
    print(output)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    print("Surface area:", area)
    return(area)


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (float(radius) ** 3)
    print("Volume:", float(volume))
    return float(volume)


def sum_n(number):
    total = 0
    for i in range(number + 1):
        total += i
    print(int(total))
    return(int(total))


def sum_n_cubes(number):
    total = 0
    for i in range(number + 1):
        total += i ** 3
    print(int(total))
    return(int(total))


def encode_better():
    message = input("Enter a message")
    word = input("Enter a key")
    messagel = []
    wordl = []
    wordl2 = []
    ad_message = []
    en_message = ''
    for letter in word:
        wordl += letter
    for i in range(len(message)):
        i = i % len(word)
        wordl2.append((ord(wordl[i])) - 65)
    for letter in message:
        messagel.append(ord(letter) - 65)
    for i in messagel:
        for j in wordl2:
            ad_message.append(((i + j) % 58) + 65)
    short_ad_message = ad_message[0:len(ad_message):len(message) + 1]
    for num in short_ad_message:
        en_message += chr(num)
    print(en_message)

if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass

"""
Name: Sean Faust
HW6.py

Problem: Working with strings - writing simple encoding functions.
Working with functions to return certain values.


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

# Takes an input from the user and prints it in American money format.
# i.e. 31.1 becomes $31.10
def cash_converter():
    number = input("Enter an integer:")
    print("That is ${:,.2f}".format(float(number)))

# Simple encoding function that adds an integer key amount to the messages
# Unicode amount per character and outputs the new string.
def encode():
    message = input("Enter a message:")
    key = input("Enter a key:")
    output = ''
    for letter in message:
        output += chr(ord(letter) + int(key))
    print(output)

# Function that finds a spheres area given the radius
def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    print("Surface area:", area)
    return area

# Function to find the spheres volume given the radius
def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (float(radius) ** 3)
    print("Volume:", float(volume))
    return float(volume)

# Function to find the sunm of all the numbers in a given range.
def sum_n(number):
    total = 0
    for i in range(number + 1):
        total += i
    return int(total)

# Function to find the sum of all numbers in a given range after they have been cubed.
def sum_n_cubes(number):
    total = 0
    for i in range(number + 1):
        total += i ** 3
    return int(total)

# Encodes a message by the unicode of a given key. If the key is shorter it repeats.
# If the key is longer it stops short. The output remains within the 57 values of A - z.
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
    print(wordl)
    for i in range(len(message)):
        i = i % len(word)
        wordl2.append((ord(wordl[i])) - 65)
    print(wordl2)
    for letter in message:
        messagel.append(ord(letter) - 65)
    print(messagel)
    for i in messagel:
        for j in wordl2:
            ad_message.append(((i + j) % 58) + 65)
    print(ad_message)
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

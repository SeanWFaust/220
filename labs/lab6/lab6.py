"""
Name: Sean Faust
Lab6.py

Problem: This lab has us working with a user inserted message and key
and outputting an encoded cipher in return.


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

def vigenere():
    length = 400
    width = 400
    win = GraphWin("Vingenere", width, length)

    rectangle = Rectangle(Point(160, 230), Point(240, 270))
    rectangle.draw(win)
    txt_pt = rectangle.getCenter()
    rec_txt = Text(Point(200, 250), 'Encode')
    rec_txt.draw(win)

    msg_msg = Text(Point(80, 50), "Message to encode:")
    msg_msg.draw(win)
    key_msg = Text(Point(80, 100), "Enter Keyword:")
    key_msg.draw(win)
    msg_enter = Entry(Point(270, 50), 25)
    msg_enter.draw(win)
    key_enter = Entry(Point(200, 100), 10)
    key_enter.draw(win)

    win.getMouse()
    rectangle.undraw()
    rec_txt.undraw()

    user_txt = msg_enter.getText()
    user_key = key_enter.getText()

    message2 = user_txt.replace(" ", "")
    word2 = user_key.replace(" ", "")
    message = message2.upper()
    word = word2.upper()

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
            ad_message.append(((i + j) % 26) + 65)
    short_ad_message = ad_message[0:len(ad_message):len(message) + 1]
    for num in short_ad_message:
        en_message += chr(num)


    result_msg = Text(Point(200, 210), "Resulting Message")
    result_msg.draw(win)
    cipher_msg = Text(Point(200, 230), en_message)
    cipher_msg.draw(win)
    close_msg = Text(Point(200, 350), "Click anywhere to close.")
    close_msg.draw(win)

    win.getMouse()
    win.close()
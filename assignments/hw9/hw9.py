"""
Name: Sean Faust
HW9.py

Problem: This homework has me making the game hangman within Python.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import random


def get_words(file_name):
    file = open(file_name, 'r')
    filelist = file.readlines()
    return filelist


def get_random_word(words):
    randword = ''
    new_words = []
    for word in words:
        new_words.append(word.replace('\n', ''))
    for word in new_words:
        randword = new_words[random.randint(0, len(new_words) - 1)]
    return randword


def letter_in_secret_word(letter, secret_word):
    for item in secret_word:
        answer = item == letter
        if answer == True:
            return answer
    return False


def already_guessed(letter, guesses):
    for item in guesses:
        answer = item == letter
        if answer == True:
            return answer
    return False


def make_hidden_secret(secret_word, guesses):
    word = ''
    for letter in secret_word:
        if letter not in guesses:
            secret_word = secret_word.replace(letter, '_')
    for letter in secret_word:
        word += letter + ' '
    word = word.rstrip()
    return word


def won(guessed):
    if '_' not in guessed:
        return True
    else:
        return False


def play_graphics(secret_word):
    width = 600
    length = 600
    win = GraphWin("Hangman", width, length)
    base = Rectangle(Point(575, 575), Point(500, 525))
    mast = Line(Point(537, 525), Point(537, 225))
    overmast = Line(Point(537, 225), Point(437, 225))
    downmast = Line(Point(437, 225), Point(437, 275))
    base.draw(win)
    mast.draw(win)
    overmast.draw(win)
    downmast.draw(win)
    info_text = Text(Point(220, 430), 'Guess a letter:')
    info_text.draw(win)
    head = Circle(Point(437, 300), 25)
    torso = Line(Point(437, 325), Point(437, 400))
    left_arm = Line(Point(437, 335), Point(417, 355))
    right_arm = Line(Point(437, 335), Point(457, 355))
    left_leg = Line(Point(437, 400), Point(417, 425))
    right_leg = Line(Point(437, 400), Point(457, 425))
    body = [head, torso, left_arm, right_arm, left_leg, right_leg]
    incr = 0
    guesses_remaining = 6
    guessed_letters = ''
    winning_text = Text(Point(300, 190), 'You won!')
    lost_text = Text(Point(300, 190), 'Sorry you did not guess the word.')
    losing_word = Text(Point(300, 210), 'The word was:{}'.format(secret_word))
    close_text = Text(Point(300, 300), 'Click anywhere to close.')
    while incr < 6:
        secreted = (make_hidden_secret(secret_word.lower(), guessed_letters))
        secret_text = Text(Point(300, 400), secreted)
        secret_text.draw(win)
        guess_info = Text(Point(300, 30), 'Guessed letters: {}'.format(guessed_letters))
        guess_info.draw(win)
        user_guess = Entry(Point(300, 430), 2)
        user_guess.draw(win)
        g_remain = Text(Point(300, 70), 'You have {} guesses remaining.'.format(guesses_remaining))
        g_remain.draw(win)
        if won(secreted):
            winning_text.draw(win)
            close_text.draw(win)
            win.getMouse()
            win.close()
        win.getKey()
        win.getKey()
        g_remain.undraw()
        guess_info.undraw()
        secret_text.undraw()
        if incr < 6:
            if user_guess.getText() in guessed_letters:
                guesses_remaining = guesses_remaining
            else:
                guessed_letters += (user_guess.getText() + ', ')
                if user_guess.getText() in secret_word:
                    guesses_remaining = guesses_remaining
                else:
                    guesses_remaining -= 1
                    incr += 1
                    body[incr - 1].draw(win)

    lost_text.draw(win)
    close_text.draw(win)
    losing_word.draw((win))
    win.getMouse()
    win.close()

    win.getMouse()
    win.close()


def play_command_line(secret_word):
    i = 0
    guessed_letters = []
    guesses_remaining = 6
    while i < 6:
        secreted = (make_hidden_secret(secret_word.lower(), guessed_letters))
        print(guessed_letters)
        print(guesses_remaining)
        print(secreted)
        if won(secreted):
            print('You won!')
            print('The word was:', secret_word)
            i = 6
        if i < 6:
            letter = input('Guess a letter:')
            guessed_letters.append(letter)
            if letter in secret_word:
                pass
            else:
                guesses_remaining -= 1
                i += 1
        if i == 6 and won(secreted) == False:
            print('Sorry, you did not guess the word.')
            print('The word was:', secret_word)



if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)

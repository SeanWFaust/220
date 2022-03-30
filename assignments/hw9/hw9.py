"""
Name: Sean Faust
HW9.py

Problem: This homework has me making the game hangman within Python.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


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
    pass


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

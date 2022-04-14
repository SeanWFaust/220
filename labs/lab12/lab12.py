from random import randint


def find_and_remove_first(list, value):
    while value in list:
        list.insert(list[value] - 1, 'Sean')
        list.remove(value)


def good_input():
    incrementer = 1
    good = 'Good input'
    while incrementer == 1:
        user_input = eval(input('Please enter a number between 1-10: '))
        if user_input >= 1 and user_input <= 10:
            incrementer = 2
        else:
            print('That number was not between 1 and 10.')
    return good


def num_digits():
    user_input = eval(input('Enter a number: '))
    while_looper = 1
    counter = 0
    while while_looper == 1:
        if user_input > 0:
            while user_input > 0:
                user_input = user_input // 10
                counter += 1
            print('Your number had {} digits!'.format(counter))
            user_input = eval(input('Enter a number: '))
        else:
            while_looper = 0


def hi_lo_game():
    number = randint(1, 10)
    while_looper = 0
    guesses_remaining = 7
    guesses = 1
    while while_looper < 7:
        user_input = eval(input('Guess a number between 1 and 10: '))
        if user_input == number:
            print('You guessed correctly! You won in ' + str(guesses) + ' guesses!')
            while_looper = 7
        elif user_input < number:
            while_looper += 1
            guesses_remaining -= 1
            guesses += 1
            print('You guessed too low. You have ' + str(guesses_remaining) + ' remaining.')
        elif user_input > number:
            while_looper += 1
            guesses_remaining -= 1
            guesses += 1
            print('You guessed too high. You have ' + str(guesses_remaining) + ' remaining.')
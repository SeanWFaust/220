"""
Name: Sean Faust
Lab9.py

Problem: Making a game with Python.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    numlist = []
    for number in range(1, 10):
        numlist.append(number)
    return numlist


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position - 1]).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    new_character = character.strip()
    new_character = new_character.lower()
    board[position - 1] = new_character


def winning_game(board):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    else:
        return False



def game_over(board):
    answer = True
    for spot in board:
        if str(spot).isnumeric():
            answer = False
    if winning_game(board) == True:
        return True
    elif answer == False:
        return False
    else:
        return True


def get_winner(board):
    x_count = board.count('x')
    o_count = board.count('o')
    if game_over(board) and x_count > o_count:
        return 'x'
    elif game_over(board) and x_count == o_count:
        return 'o'
    elif game_over(board) == False:
        return None

def play(board):
    print('x moves first. Enter the position you would like to take by entering a number 1-9.')
    user_count = 0
    characterlist = ['o', 'x']
    user_bool = input('Would you like to play tic-tac-toe?')
    if user_bool[0] == 'Y' or 'y':
        while user_bool:
            while not game_over(board):
                print_board(board)
                user_input = eval(input('Enter the position you would like to take: '))
                user_count += 1
                if is_legal(board, user_input):
                    fill_spot(board, user_input, characterlist[user_count % 2])
                else:
                    user_count -= 1
            winner = get_winner(board)
            print_board(board)
            if winning_game(board):
                print(winner + ' wins! Would you like to play again?')
            else:
                print("It's a tie!  Would you like to play again?'")
            user_bool = input('>>>')
            if user_bool[0] == 'Y' or 'y':
                user_bool = True
                board = build_board()
            else:
                user_bool = False



def main():
    play(build_board())


if __name__ == '__main__':
    main()

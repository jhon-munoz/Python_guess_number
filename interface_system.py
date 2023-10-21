from art import *
from level_system import level_info

def show_information():
    print('#' * 100)
    print(text2art("GUESS",font='block',chr_ignore=True))
    print('#' * 100)
    print(text2art('Welcome  to  the  guess  game'))
    print('The goal of the game is to guess a secret number')
    print('#' * 100)

def menu():
    tprint('Menu:')
    print('1. Show score')
    print('2. Play the game')
    print('#' * 100)


def show_game_information():
    level = level_info()
    print('First you will have to chose the level of the game you want to play')
    print('#' * 100)
    
    for index, tup in enumerate(level):
        print(f'Level {index + 1}\t-> Numbers from {tup[0]} to {tup[1]} and {tup[2]} attempts')

    print('#' * 100)


def show_score(score):
    sorted_score = sorted(score.items(), key=lambda t: int(t[1]), reverse=True)

    print(f'NAME{chr(9)}|{chr(9)}SCORE')
    print("\n".join("{}\t|\t{}".format(k, v) for k, v in sorted_score))
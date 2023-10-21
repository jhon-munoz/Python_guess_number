import random
from help_system import help_system
from general_functions import get_valid_number
from score_system import get_score
from file_system import *
from level_system import get_level
from interface_system import *
import threading
import queue

stop_thread = threading.Event()

def execute_game():
    continue_game = True
    show_game_information()
    lower_bound, upper_bound, trials_number, level = get_level()
    user_name = input('Please type your name: ')

    while(continue_game):
        print('#' * 100)
        print(f'Your current level is : {level}')
        secret_number = random.randint(lower_bound,upper_bound)

        user_win = False
        trials_done = 0

        for i in range(trials_number):    
            trials_done += 1
            user_guess_queue = queue.Queue()       

            print('#' * 100)
            print(f'You have {trials_number - i} attempts to guess the number')                          
        
            #Wait 20 seconds for finishing the task
            task = threading.Thread(target= guess, args=(lower_bound,upper_bound, user_guess_queue))
            task.start()
            task.join(timeout=50) #Wait 50 seconds

            if task.is_alive():
                stop_thread.set()
                continue
            
            user_guess = user_guess_queue.get()            

            if user_guess is not None and user_guess != secret_number:
                help_system(user_guess, secret_number)
            else:
                user_win = True
                break

        if user_win:
            tprint('You won!')
            level += 1
            lower_bound, upper_bound, trials_number = level_info()[level - 1]
        else:
            tprint('You lose!')
            continue_game = False
    
        score = get_score(trials_done,level)
        save_score(user_name,score)
        print(f'{user_name}, your score is: {score}')


def guess(lower_bound, upper_bound, user_guess_queue):
    user_guess = get_valid_number(lower_bound, upper_bound, "guess")
    user_guess_queue.put(user_guess)



def select_option():
    option = int(input('Select the option you prefer: '))
    match option:
        case 1:
            show_score(get_total_score())
        case 2:
            execute_game()
        case _:
            print('You did not select the correct option')
        



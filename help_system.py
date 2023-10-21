def is_prime(secret):
    for n in range(2, secret):
        if secret % n == 0:
            return 'The secret number is not prime'
    return 'The secret number is prime'

def is_even(secret):
    if secret % 2 == 0:
        return 'The secret number is even'
    else:
        return 'The secret number is odd'
    
def is_divisible_by_four(secret):
    if secret % 4 == 0:
        return 'The secret number is divisible by 4'
    else:
        return 'The secret number is not divisible by 4'
    
def numbers_validation(guess, secret):
    if guess > secret:
        print('Too high')
    elif guess < secret:
        print('Too low')

def help_system(guess, secret):
    numbers_validation(guess, secret)
    print(is_prime(secret))
    print(is_even(secret))
    print(is_divisible_by_four(secret))
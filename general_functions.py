def get_valid_number(minimum_number, maximum_number, prompt):
    is_valid_input = False
    while not is_valid_input:
        try:
            valid_number = int(input(f'Write the {prompt} number: '))
        except ValueError as exception_info:
            print(exception_info)
            print('Your input is not valid, it mus be a numeric value.')
            continue

        if minimum_number <= valid_number <= maximum_number:
            is_valid_input = True
        else:
            print(f'Your input is not valid, it must be greater or equal than {minimum_number} and minor than {maximum_number}. Try again.')

    return valid_number

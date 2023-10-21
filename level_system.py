from general_functions import get_valid_number

# level_1 = (1,100,10)
# level_2 = (1,500,7)
# level_3 = (1,1000,5)
level_1 = (1,10,5)
level_2 = (1,50,10)
level_3 = (1,50,5)
level_4 = (1,100,10)
level_5 = (1,200,12)
level_6 = (1,200,7)
level_7 = (1,500,12)
level_8 = (1,500,7)
level_9 = (1,1000,10)
level_10 = (1,1000,5)


def level_info():
    return [
        level_1,
        level_2,
        level_3,
        level_4,
        level_5,
        level_6,
        level_7,
        level_8,
        level_9,
        level_10
    ]


def get_level():
    level = get_valid_number(1, 3, 'correct level')

    lower_bound, upper_bound, trials_number = level_info()[level - 1]

    # match level:
    #     case 1:
    #         lower_bound, upper_bound, trials_number = level_1
    #     case 2:
    #         lower_bound, upper_bound, trials_number = level_2
    #     case 3:
    #         lower_bound, upper_bound, trials_number = level_3

    return lower_bound, upper_bound, trials_number, level
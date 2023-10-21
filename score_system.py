from level_system import *

max_score = 0

def get_score(attempt, level):
    max_score = level_info()[level - 1][1]

    # match level:
    #     case 1:
    #         max_score = level_1[1]
    #     case 2:
    #         max_score = level_2[1]
    #     case 3:
    #         max_score = level_3[1]

    return int(max_score/attempt)
    
    
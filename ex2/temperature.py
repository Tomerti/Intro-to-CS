#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that checks if  at least
# 2 out of 3 given temperatures are higher than an other given temperature.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
def is_vormir_safe(min_temp, temp1, temp2, temp3):
    '''A simple program that checks if  at least
    2 out of 3 given temperatures are higher than
    an other given temperature.'''
    if temp1 > min_temp and temp2 > min_temp:
        return True
    elif temp1 > min_temp and temp3 > min_temp:
        return True
    elif temp2 > min_temp and temp3 > min_temp:
        return True
    return False
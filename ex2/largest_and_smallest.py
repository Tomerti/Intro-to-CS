#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def largest_and_smallest(num1, num2, num3):
    '''Function that gets 3 numbers, and returns
    the maximal and minimal values'''
    if num1 > num2:
        max = num1
        if num2 > num3:
            min = num3
            return max, min
        else:
            min = num2
            if num1<num3:
                max = num3
                return max, min
            else:
                return max,min
    else:
        max=num2
        if num1 > num3:
            min = num3
            return max, min
        else:
            min = num1
            if num2<num3:
                max = num3
                return max, min
            else:
                return max, min

def check_largest_and_smallest():
    '''Function that checks largest and smallest function,
    deilvers 3 numbers and expects certain results.'''
    # I chose 2,2,2 to make sure if works when all numbers are identical
    # I chose -1,2,3 to make sure if works with negative numbers
    bool=True
    if largest_and_smallest(17, 1, 6) != (17, 1):
        bool = False
    if largest_and_smallest(1, 1, 2) != (2, 1):
        bool = False
    if largest_and_smallest(2, 2, 2) != (2,2):
        bool = False
    if largest_and_smallest(-1,2,3) != (3,-1):
        bool = False
    return bool
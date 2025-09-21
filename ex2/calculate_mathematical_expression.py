#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that receives 2 numbers and an operator,
# and returns the value of the mathematical expression.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def calculate_mathematical_expression(number1, number2, operator):
    '''Function that receives 2 numbers and an operator(+,-,*,:), returns the
    value of the mathematical expression.'''
    if operator == "+":
        return (number1 + number2)
    elif operator == "-":
        return (number1 - number2)
    elif operator == "*":
        return (number1 * number2)
    elif operator == ":":
        if (number2 != 0):
            return number1 / number2
        return None
    return None


def calculate_from_string(math_str):
    '''Function that receives a mathematical expression as a string in
    template of "<number1> <operator> <number2>", and returns the value
    of the expression, the function calls
    calculate_mathematical_expression function'''
    number1, operator, number2 = math_str.split()
    number1 = float(number1)
    number2 = float(number2)
    return calculate_mathematical_expression(number1, number2, operator)

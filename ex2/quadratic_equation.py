#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that get a,b,c values and
# returns the value of the quadratic equation, also when
# received as a string
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
import math
def quadratic_equation(factor_pow,factor_reg,free_num):
    '''Function that gets a,b,c values and returns the value of
    the quadratic equation'''
    if factor_pow != 0:
        delta_square = math.pow(factor_reg, 2) - 4 * (factor_pow * free_num)

        if delta_square >= 0:
            quad_square = math.sqrt(delta_square)
            val1 = (-factor_reg + quad_square) / (2 * factor_pow)
            val2 = (-factor_reg - quad_square) / (2 * factor_pow)
        else:
            return None, None
    else:
        return None, None
    if val1 != val2:
        return val1, val2
    return val1, None

def quadratic_equation_user_input():
    '''Function that gets a string from user, returns the value of the
     quadratic equation'''
    a, b, c = input("Insert coefficients a, b, and c: ").split()
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        print("The parameter 'a' may not equal 0")
    else:
        val1,val2 = quadratic_equation(a, b, c)
        if val1 != val2 and val2 != None:
            print("The equation has 2 solutions:",val1,"and",val2)
        elif val1 != val2 and val2 == None:
            print("The equation has 1 solution:",val1)
        if val1 == val2 and val1 == None:
            print("The equation has no solutions")
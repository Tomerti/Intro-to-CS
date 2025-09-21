#################################################################
# FILE : math_print.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that uses math module commands
# in order to calculate the golden ratio, six squared,
# hypotenuse, pi, e and squares area when sides are 1-10.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: https://docs.python.org/3/library/math.html
# NOTES: ...
#################################################################
import math

def golden_ratio():
    '''Part A - calculates and prints the golden ratio.'''
    print((1+math.sqrt(5))/2)

def six_squared():
    '''Part B - Calculates and prints six squared (6**2)'''
    print(math.pow(6,2))

def hypotenuse():
    '''Part C - calculates and prints the hypotenuse of a
    triangle when first side is 5, second side is 12'''
    print(math.hypot(5,12))

def pi():
    '''Part D - prints value of pi.'''
    print(math.pi)

def e():
    '''Part E - prints value of e.'''
    print(math.e)

def squares_area():
    '''Part F - calculates and prints area of squares, sides are 1-10.'''
    print(math.pow(1,2), math.pow(2,2), math.pow(3,2), math.pow(4,2),
          math.pow(5,2), math.pow(6,2), math.pow(7,2),
          math.pow(8,2), math.pow(9,2), math.pow(10,2))

if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
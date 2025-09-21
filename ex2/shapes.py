#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that asks user to choose from
# given set of shapes, gets relevant information about it
# and returns the value of the area of the given shape and information.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
import math

def shape_area():
    '''Function that asks user to choose from given set of shapes,
    gets relevant information about that shape, calculates
    and returns the value of the are of the given shape and information.'''
    shape=input(("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if shape == "1":
        radius = float(input()) #gets radius of the circle
        area = math.pi * math.pow(radius,2)
        return area
    elif shape == "2":
        side_a = float(input()) #gets side A of the rectangle
        side_b = float(input()) #gets side B of the rectangle
        area = side_a * side_b
        return area
    elif shape == "3":
        side = float(input()) #gets side of the equilateral triangle
        area = (math.sqrt(3) / 4) * math.pow(side,2)
        return area
    return None
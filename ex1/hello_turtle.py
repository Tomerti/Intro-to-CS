#################################################################
# FILE : hello_turtle.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that uses Python's turtle module,
# drawing 3 flowers that has 4 petals.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
import turtle

# Part A - drawing a petal:
def draw_petal():
    '''Function that draws a petal using turtle commands.'''
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

# Part B - drawing a flower:
def draw_flower():
    '''Function that draws a flower, using draw_petal function.'''
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

# Part C - Drawing a flower and advancing:
def draw_flower_and_advance():
    '''Function that draws a flower and fixes turtle location
     to a new one.'''
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


# Part D - Drawing a bed of flowers:
def draw_flower_bed():
    '''Function that draws 3 flowers while advancing to
    new locations, using draw_flower_and_advance function'''
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()

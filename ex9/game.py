from car import *
from board import *
from helper import *
import sys

#################################################################
# FILE : game.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: Program that holds a game object, to play the game
# Rush Hour
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
class Game:
    """
    Class that represents the game rush hour, has cars and cool board
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        #You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.__board = board


    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        temp_holder_str = input("Please insert car color and movement \n")
        if(temp_holder_str == "!"):
            return "Done"
        if ("," not in temp_holder_str):
            print("There's a problem")
            return "There's a problem"
        temp_holder_lst = temp_holder_str.split(",")
        car_color = temp_holder_lst[0]
        car_move = temp_holder_lst[1]
        if self.__board.move_car(car_color, car_move):
            if self.__board.cell_content\
                        (self.__board.target_location()) is not None:
                print("You Won!")
                return "You Won!"
            else:
                print(self.__board)
                return "Move Successful"
        else:
            print("There's a problem")
            return "There's a problem"







    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(self.__board)
        wanna_play = True
        while wanna_play:
            message = self.__single_turn()
            if message == "You Won!" or message == "Done":
                return




if __name__== "__main__":
    json_path = sys.argv[1]
    json = load_json(json_path)
    valid_names = ["R","G","W","O","B","Y"]
    board = Board()
    for name in json:
        if name in valid_names:
            length = json[name][0]
            if 2 <= length <= 4:
                row = json[name][1][0]
                col = json[name][1][1]
                location = (row, col)
                orientation = json[name][2]
                if 0 <= orientation <= 1:
                    car = Car(name, length, location, orientation)
                    board.add_car(car)

    game = Game(board)
    game.play()

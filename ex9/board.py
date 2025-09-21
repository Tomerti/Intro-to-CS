#################################################################
# FILE : board.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: Program that holds a board object
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################
class Board:
    """
    Class of board for the game, made of 7 * 7 with graphical attribute.
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.__gboard = [["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "E"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"]]
        self.__carslist = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        sentences = list()
        for i in range (len(self.__gboard)):
            sentences.append("".join(self.__gboard[i]))
        return "\n".join(sentences)



    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        #In this board, returns a list containing the cells in the square
        #from (0,0) to (6,6) and the target cell (3,7)
        coordinates_list = []
        for i in range(7):
            for k in range(7):
                coordinates_list.append((i,k))
        coordinates_list.append((3,7))
        return coordinates_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        best_list = list()
        for car in self.__carslist:
            temp_move_dict = car.possible_moves()
            for key in temp_move_dict:
                lst_of_cells = car.movement_requirements(key)
                for cell in lst_of_cells:
                    row, col = cell
                    if (self.cell_content(cell) is None and 0 <= row <= 6 and
                        0 <= col <= 6) or (row == 3 and col == 7):
                        best_list.append((car.get_name(), key,
                                          temp_move_dict[key]))
        return best_list





    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        #In this board, returns (3,7)
        return 3,7

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        for car in self.__carslist:
            if coordinate in car.car_coordinates():
                return car.get_name()
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        #Remember to consider all the reasons adding a car can fail.
        #You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        result = True
        car_name = car.get_name()
        for other_car in self.__carslist:
            if other_car.get_name() == car_name:
                return False

        car_coordinates = car.car_coordinates()
        for coordinate in car_coordinates:
            row1, col1 = coordinate
            if self.cell_content(coordinate)\
                    is not None or\
                    row1 < 0 or row1 > 6 or col1 < 0 or col1 > 6:
                result = False
        if result is True:
            self.__carslist.append(car)
            for coordinate in car_coordinates:
                row, col = coordinate
                self.__gboard[row][col] = car_name
        return result






    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        for car in self.__carslist:
            if name == car.get_name():
                if movekey in car.possible_moves():
                    lst_cells = car.movement_requirements(movekey)
                    for cell in lst_cells:
                        if cell in self.cell_list() and\
                                self.cell_content(cell) is None:
                            car.move(movekey)
                            self.restart_board()
                            for possible_car in self.__carslist:
                                for coordinate \
                                        in possible_car.car_coordinates():
                                    row, col = coordinate
                                    self.__gboard[row][col] = \
                                        possible_car.get_name()
                            return True
        return False

    def restart_board(self):
        self.__gboard = [["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "E"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"],
                         ["_", "_", "_", "_", "_", "_", "_", "*"]]

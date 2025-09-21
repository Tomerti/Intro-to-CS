#################################################################
# FILE : car.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: Program that holds a car object
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

class Car:
    """
    Car class that has name length location and orientation,
    several methods
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.__name = name
        self.__length = int(length)
        self.__location = tuple(location)
        self.__orientation = int(orientation)

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates_list = []
        row, col = self.__location
        if self.__orientation == 0:
            for i in range(self.__length):
                coordinates_list.append((row + i, col))
        else:
            for i in range(self.__length):
                coordinates_list.append((row, col + i))

        return sorted(coordinates_list)

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        dict_of_moves = dict()
        if self.__orientation == 0:
            dict_of_moves["u"] = "Cause the car to go up."
            dict_of_moves["d"] = "Cause the car to go down."
        if self.__orientation == 1:
            dict_of_moves["l"] = "Cause the car to go left."
            dict_of_moves["r"] = "Cause the car to go right."

        return dict_of_moves

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        #For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        #be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        temp_lst = []
        row, col = self.__location
        if movekey == "u":
            if self.__orientation == 0:
                return [(row - 1, col)]
            if self.__orientation == 1:
                for coordinate in self.car_coordinates():
                    row1, col1 = coordinate
                    temp_lst.append((row1 - 1, col1))
        if movekey == "d":
            if self.__orientation == 0:
                return [(row + self.__length, col)]
            if self.__orientation == 1:
                for coordinate in self.car_coordinates():
                    row1, col1 = coordinate
                    temp_lst.append((row1 + 1, col1))
        if movekey == "l":
            if self.__orientation == 1:
                return [(row, col - 1)]
            if self.__orientation == 0:
                for coordinate in self.car_coordinates():
                    row1, col1 = coordinate
                    temp_lst.append((row1, col1 - 1))
        if movekey == "r":
            if self.__orientation == 1:
                return [(row, col + self.__length)]
            if self.__orientation == 0:
                for coordinate in self.car_coordinates():
                    row1, col1 = coordinate
                    temp_lst.append((row1, col1 + 1))
        return temp_lst

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey in self.possible_moves():
            row, col = self.__location
            if movekey == "u" and self.__orientation == 0:
                self.__location = (row - 1, col)
            elif movekey == "d" and self.__orientation == 0:
                self.__location = (row + 1, col)
            elif movekey == "l" and self.__orientation == 1:
                self.__location = (row, col - 1)
            elif movekey == "r" and self.__orientation == 1:
                self.__location = (row, col + 1)
            return True
        else:
            return False


    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name

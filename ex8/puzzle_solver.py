from typing import List, Tuple, Set, Optional
import copy

#################################################################
# FILE : puzzle_solver.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex8 2021
# DESCRIPTION: program that uses backtracking methods to solve
# puzzles
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

# We define the types of a partial picture and a constraint
#(for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    '''Function that gets a board, specific cell coordinates
        and returns the max seen cells option of it'''
    if picture[row][col] == 0:
        return 0
    seen = 1

    bot_distance = len(picture) - row - 1
    right_distance = len(picture[0]) - col - 1

    for i in range(row):
        if picture[row - 1 - i][col] == 0:
            break
        seen += 1

    for i in range(bot_distance):
        if picture[row + 1 + i][col] == 0:
            break
        seen += 1

    for i in range(col):
        if picture[row][col - 1 - i] == 0:
            break
        seen += 1

    for i in range(right_distance):
        if picture[row][col + 1 + i] == 0:
            break
        seen += 1
    return seen


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    '''Function that gets a board, specific cell coordinates
            and returns the min seen cells option of it'''
    if picture[row][col] != 1:
        return 0
    seen = 1

    bot_distance = len(picture) - row - 1
    right_distance = len(picture[0]) - col - 1

    for i in range(row):
        if picture[row - 1 - i][col] != 1:
            break
        seen += 1

    for i in range(bot_distance):
        if picture[row + 1 + i][col] != 1:
            break
        seen += 1

    for i in range(col):
        if picture[row][col - 1 - i] != 1:
            break
        seen += 1

    for i in range(right_distance):
        if picture[row][col + 1 + i] != 1:
            break
        seen += 1
    return seen


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) ->\
        int:
    '''Function that gets a board, some constraints and tells if the
        board fits the constraints in a sort of way,
        0 if does not fit one of the constraints, 1 if fits all of them
        exactly, and 2 if fits all of them in more than 1 way'''
    list_of_results = []
    for constraint in constraints_set:
        row = constraint[0]
        col = constraint[1]
        seen = constraint[2]
        max_seen = max_seen_cells(picture, row, col)
        min_seen = min_seen_cells(picture, row, col)
        if seen > max_seen or seen < min_seen:
            return 0
        if seen == max_seen and seen == min_seen:
            list_of_results.append(1)
        else:
            list_of_results.append(2)
    if 2 in list_of_results:
        return 2
    return 1


def create_empty_picture(n: int, m: int) -> List[List[int]]:
    '''Function that gets 2 values, n and m,
    returns a 2dimensional list '''
    picture = []
    rows = n
    cols = m
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(-1)
        picture.append(col)
    return picture


def _solve_puzzle(picture: List[List[int]], constraints_set: \
        Set[Tuple[int, int, int]], index) -> Optional[List[List[int]]]:
    '''Helper function that gets a picture and constraints set and index,
    returns a solution for the picture with given constraints'''
    if index == len(picture) * len(picture[0]):
        return picture

    row = index // len(picture[0])
    col = index % len(picture[0])

    if picture[row][col] != -1:
        _solve_puzzle(picture, constraints_set, index + 1)
        return picture

    for i in range(2):
        picture[row][col] = i
        if check_constraints(picture, constraints_set) != 0:
            _solve_puzzle(picture, constraints_set, index + 1)
        if check_constraints(picture, constraints_set) == 1:
            return picture
    picture[row][col] = -1


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) ->\
        Optional[Picture]:
    '''Function that gets a constraints set, two numbers,
        creates a partial picture and returns a solved puzzle'''
    picture = create_empty_picture(n, m)
    return _solve_puzzle(picture, constraints_set, 0)


def _how_many_solutions(picture: List[List[int]], constraints_set: \
        Set[Tuple[int, int, int]], index, counter) -> int:
    '''Helper for how many solutions, counts how many solutions are
    possible for given picture with certain constraints and returns it'''
    if index == len(picture) * len(picture[0]):
        counter += 1
        return counter

    row = index // len(picture[0])
    col = index % len(picture[0])

    if picture[row][col] != -1:
        counter += _how_many_solutions(picture, constraints_set, index + 1, 0)
        return counter

    for i in range(2):
        picture[row][col] = i
        if check_constraints(picture, constraints_set) != 0:
            counter += _how_many_solutions(picture,
                                           constraints_set, index + 1, 0)
    picture[row][col] = -1
    return counter


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) ->\
        int:
    '''Function that gets a set of constraints, two numbers, returns
        how many possible solutions are for that puzzle'''
    picture = create_empty_picture(n, m)
    return _how_many_solutions(picture, constraints_set, 0, 0)


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    '''Function that gets a picture, returns a set of constraints for
        given picture. when each of constraints is crucial for the puzzle.'''
    constraints_set = set()
    new_constraints_set = set()
    copied_picture = copy.deepcopy(picture)
    rows = len(picture)
    columns = len(picture[0])
    for row in range(rows):
        for col in range(columns):
            if max_seen_cells(copied_picture, row, col) == \
                    min_seen_cells(copied_picture, row, col):
                constraints_set.add((row, col,
                                     max_seen_cells(copied_picture, row, col)))

    for constraint in constraints_set:
        new_constraints_set.add(constraint)
        if how_many_solutions(new_constraints_set, rows, columns) == 1:
            return new_constraints_set

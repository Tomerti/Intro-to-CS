from ex7_helper import *
from typing import Any
from typing import List
#################################################################
# FILE : ex7.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex7 2021
# DESCRIPTION: program the does different functions using only recursion
#
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################



def mult(x : float, y : int) -> float:
    '''Gets two numbers, returns the multiplication of them'''
    if y == 1:
        return x
    return add(x, mult(x,subtract_1(y)))


def is_even(n : int) -> bool:
    '''Gets a number, returns True if even, False if odd'''
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(subtract_1(subtract_1(n)))


def is_divisable(divisor : float, divisor2 : float, divided : int) -> bool:
    '''Gets a number says if divisable by the other'''
    print(divisor, divisor2, divided)
    if divisor == divided:
        return True
    if divisor > divided:
        return False
    return is_divisable(add(divisor,divisor2),divisor2, divided)


def log_mult(x : float, y : int) -> float:
    '''Multiplies two numbers in O(lonN) complexity'''
    if y == 1:
        return x
    p = log_mult(x, divide_by_2(y))
    if not is_odd(y):
        return add(p,p)
    else:
        return add(add(p,p),x)


def is_power_helper(acc: float, b: int, x: int) -> bool:
    '''Helper function to check is one number is a power of the other'''
    if acc < x:
        return is_power_helper(log_mult(acc, b), b, x)
    return acc == x


def is_power(b: int, x:int) -> bool:
    '''Gets a number b, tells if X is a result of power of b'''
    return is_power_helper(b, b, x)


def reverse_helper(s: str, s2: str, n: int) -> str:
    '''Helper function for reverse'''
    if n == 0:
        return s2
    s2 = append_to_end(s2, s[subtract_1(n)])
    n = subtract_1(n)
    return reverse_helper(s, s2, n)


def reverse(s : str) -> str:
    '''Gets a string, returns a new, reversed string'''
    s2 = ""
    n = len(s)
    return reverse_helper(s, s2, n)


def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> Any:
    '''Runs a game of hanoi towers'''
    if n<1:
        return
    if n == 1:
        Hanoi.move(src,dst)
        return
    play_hanoi(Hanoi, subtract_1(n), src, temp, dst)
    Hanoi.move(src,dst)
    play_hanoi(Hanoi, subtract_1(n), temp, dst, src)


def count_in_number(n: int, sum: int) -> int:
    '''Checks how many 1 in given number'''
    if n == 0:
        return sum

    if n % 10 == 1:
        sum += 1
    return count_in_number(n//10, sum)


def number_of_one_helper(n: int, sum : int) -> int:
    '''Helper function to check how many 1 till n number'''
    if n == 0:
        return sum
    sum += count_in_number(n, 0)
    return number_of_one_helper(subtract_1(n), sum)


def number_of_ones(n: int) -> int:
    '''Checks how many 1's till N number'''
    sum = 0
    return number_of_one_helper(n, sum)


def compare_2d_lists_helper2(tl1: List[int], tl2: List[int], n: int) -> bool:
    '''Helper which checks for every cell in 2 lists if identical'''
    if n == -1:
        return True
    if tl1[n] != tl2[n]:
        return False
    return compare_2d_lists_helper2(tl1, tl2, subtract_1(n))


def compare_2d_lists_helper(l1: List[List[int]], l2: List[List[int]],
                            size: int) -> bool:
    '''Helper which checks for every list in 2 lists if identical'''
    if size == -1:
        return True
    if len(l1[size]) != len(l2[size]):
        return False
    n = subtract_1(len(l1[size]))
    if not compare_2d_lists_helper2(l1[size], l2[size], n):
        return False
    return compare_2d_lists_helper(l1, l2, subtract_1(size))


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    '''Function that gets 2d lists and returns True if identical'''
    if len(l1) != len(l2):
        return False
    size = subtract_1(len(l1))
    return compare_2d_lists_helper(l1, l2, size)

def magic_list(n:int) -> List[Any]:
    '''Function that gets a number and returns a magic list out of it'''
    if n == 0:
        return []
    l1 = magic_list(subtract_1(n))
    l1.append(magic_list(subtract_1(n)))
    return l1
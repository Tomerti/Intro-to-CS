#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Tomer Titinger , tomer.titinger , 208611939
# EXERCISE : intro2cs2 ex3 2020
# DESCRIPTION: Exercise 3 contains different functions about
# lists and so, performing various actions on them, also contains
# prime numbers checks and more.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

def input_list():
    '''Function that receives numbers from user, returns a list of
    all the numbers received as floats.'''
    ls = []
    total_of_nums = 0
    while True:
        given_str = input()
        if given_str == "":
            if len(ls) == 0:
                ls.append(0)
                return ls
            ls.append(total_of_nums)
            return ls
        given_num = float(given_str)
        total_of_nums += given_num
        ls.append(given_num)

def inner_product(vec_1, vec_2):
    '''Function that gets two lists of floats/integers
    and return the total value of synced blocks
    of the functions. first times first, second times second...'''
    total = 0
    if len(vec_1) != len(vec_2):
        return None # by definition of exercise
    if len(vec_1) == 0 and len(vec_2) == 0:
        return total # total is 0
    vecs_len = range(len(vec_1))
    for i in vecs_len:
        total += vec_1[i] * vec_2[i]
    return total

def sequence_up(sequence):
    ''' Function that checks if sequence goes up.'''
    sequence_len = range(len(sequence)-1)
    for i in sequence_len:
        if sequence[i] > sequence[i+1]:
            return False
    return True

def sequence_very_up(sequence):
    '''Function that checks if sequence goes very up.'''
    sequence_len = range(len(sequence)-1)
    for i in sequence_len:
        if sequence[i] >= sequence[i+1]:
            return False
    return True

def sequence_down(sequence):
    '''Function that checks if sequence goes down.'''
    sequence_len = range(len(sequence)-1)
    for i in sequence_len:
        if sequence[i] < sequence[i+1]:
            return False
    return True

def sequence_very_down(sequence):
    '''Function that checks if sequence goes very down.'''
    sequence_len = range(len(sequence)-1)
    for i in sequence_len:
        if sequence[i] <= sequence[i+1]:
            return False
    return True

def sequence_monotonicity(sequence):
    '''Function that checks the monotonicity of a sequence.'''
    # ls[0] - every item is bigger than or equal to the previous
    # ls[1] - every item is bigger than the previous
    # ls[2] - every item is smaller than or equal the previous
    # ls[3] - every is smaller than the previous
    ls = [True, True, True, True]
    if(len(sequence) == 0):
        return ls # returns [True, True, True, True]
    if sequence_up(sequence) != True:
        ls[0] = False
    if sequence_very_up(sequence) != True:
        ls[1] = False
    if sequence_down(sequence) != True:
        ls[2] = False
    if sequence_very_down(sequence) != True:
        ls[3] = False
    return ls

def monotonicity_inverse(def_bool):
    '''Function that gets a list of booleans and return sequence that
    fits them.'''
    if def_bool == [True, True, False, False]:
        return [1, 2, 3, 4]
    elif def_bool == [True, False, False, False]:
        return [1, 1, 2, 3]
    elif def_bool == [False, False, True, True]:
        return [4, 3, 2, 1]
    elif def_bool == [False, False, True, False]:
        return [3, 3, 2, 1]
    elif def_bool == [True, False, True, False]:
        return [1, 1, 1, 1]
    elif def_bool == [False, False, False, False]:
        return [1, 2, 1, 2]
    return None


def is_prime(n):
    '''Function that checks if a number is prime'''
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    sqr_n = int((n ** 1 / 2)) + 1
    for i in range(2, sqr_n):
        if n % i == 0:
            return False
    return True


def primes_for_asafi(n):
    '''Function that gets a <number>,
    returns a list which has <number> prime numbers'''
    counted_primes = 0
    primes_list = []
    counter = 0
    while counted_primes < n:
        if is_prime(counter):
            primes_list.append(counter)
            counted_primes += 1
        counter += 1
    return primes_list


def sum_of_vectors(vec_lst):
    '''Function that gets 2 vectors and returns a new vector
    which represents their summary
    <cell 1 of vector1> + <cell 1 of vector2> = <cell1> of vector3'''
    ls = []
    if (len(vec_lst) == 0):
        return None

    for i in range(len(vec_lst)):
        if vec_lst[i] == []:
            return None

    for k in range(len(vec_lst[i])):
        ls.append(0)

    for i in range(len(vec_lst)):
        for k in range(len(vec_lst[i])):
            ls[k] += vec_lst[i][k]
    return ls

def num_of_orthogonal(vectors):
    '''Function that gets a list of vectors, checks and counts the number
    of pairs that multiplication result is 0'''
    couples_count = 0
    for i in range(len(vectors)):
        for k in range(i+1,len(vectors)):
            if inner_product(vectors[i], vectors[k]) == 0:
                couples_count += 1
    return couples_count

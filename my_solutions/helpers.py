import itertools
import numpy as np


ROW = 0
COL = 1


class Coordinates2D():
    def __init__(self, numbers):
        self.x = numbers[0]
        self.y = numbers[1]
        self.list = [numbers[0], numbers[1]]
        self.tuple = (numbers[0], numbers[1])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.x},{self.y}"


class Grid():
    '''Examples of usefull numpy methods:
        np.where(condition) -> returns indexes where condition is met
        np.where(np_matrix == number) -> [[i1_row, i2_row], [i1_col, i2_col]]

        np.any(condition) -> returns boolean if any element meets condition
        np.all(condition) -> returns boolean if all elements meet condition
        np.all(np_matrix > number) -> False
        np.all(np_matrix > number, axis=Grid.row_axis) -> [ True False False False False]
    '''
    col_axis = 0
    row_axis = 1

    def get_from_string(string, type, split=None):
        '''Returns a numpy matrix from a single plain string.
        String's rows must be separated by '\n'. Callback defines row elements splitting.'''
        if not split:
            split = lambda row: row.split()
        return np.asarray([split(row) for row in string.split("\n")], dtype=type)

    def create_filled_with(shape, value):
        '''Returns a matrix of given shape filled with given value.
        Example: create_filled_with((10, 10), 0)'''
        return np.full(shape, value)

    def get_index_tuples_where(result):
        '''Returns a list of index tuples for given results of numpy's where method.
        Example: get_index_tuples_where(np.where(matrix > 0))'''
        indexes = []
        for i in range(len(result[0])):
            row = result[ROW][i]
            col = result[COL][i]
            indexes.append((row, col))
        return indexes

    def sum(matrix):
        '''Returns the sum of all matrix elements.'''
        return np.sum(matrix)


def is_int(object):
    return (isinstance(object, int))

def is_float(object):
    return (isinstance(object, float))

def is_number(object):
    return is_int(object) or is_float(object)

def is_str(object):
    return (isinstance(object, str))

def is_list(object):
    return (isinstance(object, list))

def is_dict(object):
    return (isinstance(object, dict))

def str_to_int(object):
    if object.isdigit():
        return int(object)
    else:
        return object

def invert_binary(binary_str):
    '''Returns a string with the inverse of given binary string.
    Example: invert_binary("101011") -> 010100'''
    inverse_int = int(binary_str, 2) ^ (2 ** (len(binary_str) + 1) - 1)
    return bin(inverse_int)[3:]

def groupby(object):
    return [
        {"element": k, "occurrences": list(v)}
        for k, v in itertools.groupby(object)
    ]

def get_subsets_in_sequence(set, length):
    '''Returns a list of subsets in sequence of given length.
    Example:
        get_sequenced_subsets([0, 1, 2, 3, 4, 5], 3)
        return -> [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]'''
    return [set[i:i + 3] for i in range(len(set) - (length - 1))]

def get_unique_permutations(elements):
    reversed_permutations = set()
    unique_permutations = []
    for permutation in itertools.permutations(elements):
        if permutation not in reversed_permutations:
            reversed_permutations.add(tuple(reversed(permutation)))
            unique_permutations.append(permutation)
    return unique_permutations

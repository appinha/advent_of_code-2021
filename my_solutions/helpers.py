import re
import itertools
import numpy as np


X = 0
Y = 1

ROW = 0
COL = 1


class Coordinates2D():
    def __init__(self, data):
        self.x, self.y = self.get_coordinates(data)
        self.list = [self.x, self.y]
        self.tuple = (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"({self.x},{self.y})"

    def get_coordinates(self, data):
        if type(data) == list:
            return data[0], data[1]
        return Coordinates2D.get_tuple_from_string(data)

    def get_tuple_from_string(string):
        return tuple(find_all_integers(string))

    def get_max_from_tuples(tuples):
        return max(x for x, _ in tuples), max(y for _, y in tuples)


class Line():
    def __init__(self, string, spacer=None):
        self.start, self.end = self.get_coordinates(string, spacer)
        self.min_x, self.max_x = sorted([self.start.x, self.end.x])
        self.min_y, self.max_y = sorted([self.start.y, self.end.y])

    def get_coordinates(self, string, spacer):
        if spacer:
            string = string.replace(spacer, " ")
        numbers = find_all_integers(string)
        return Coordinates2D(numbers[0:2]), Coordinates2D(numbers[2:])

    def is_horizontal(self):
        return self.start.x != self.end.x and self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x and self.start.y != self.end.y

    def is_diagonal(self):
        return self.start.x != self.end.x and self.start.y != self.end.y

    def get_points(self):
        if self.is_horizontal():
            return [(x, self.start.y) for x in range(self.min_x, self.max_x + 1)]
        if self.is_vertical():
            return [(self.start.x, y) for y in range(self.min_y, self.max_y + 1)]
        if self.is_diagonal():
            (x1, y1), (x2, y2) = sorted([self.start.tuple, self.end.tuple])
            return ((x1 + x, y1 + x) for x in range((x2 + 1) - x1))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Line: {self.start} -> {self.end}"


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

def lst_to_str(object):
    return ''.join(object)

def flatten_list(list2D):
    return list(itertools.chain(*list2D))

def find_all_integers(string):
    return list(map(int, re.findall(r'[0-9\-]+', string)))

def find_all_positive_integers(string):
    return list(map(int, re.findall(r'\d+', string)))

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
    return [set[i:i + length] for i in range(len(set) - (length - 1))]

def get_unique_permutations(elements):
    reversed_permutations = set()
    unique_permutations = []
    for permutation in itertools.permutations(elements):
        if permutation not in reversed_permutations:
            reversed_permutations.add(tuple(reversed(permutation)))
            unique_permutations.append(permutation)
    return unique_permutations

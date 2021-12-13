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
    def __init__(self):
        pass

    def get_from_string(string, type, split=None):
        '''Returns a numpy matrix from a single plain string.
        String's rows must be separated by '\n'. Callback defines row elements splitting.'''
        if not split:
            split = lambda row: row.split()
        return np.asarray([split(row) for row in string.split("\n")], dtype=type)

    def get_index_tuples_where(result):
        '''Returns a list of index tuples for given results of numpy's where method.
        Example: get_index_tuples_where(np.where(matrix > 0))'''
        indexes = []
        for i in range(len(result[0])):
            row = result[ROW][i]
            col = result[COL][i]
            indexes.append((row, col))
        return indexes


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

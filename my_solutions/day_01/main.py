import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from helpers import get_subsets_in_sequence


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def _get_numbers(self, raw_input):
        return list(map(int, raw_input))

    def _count_increases(self, numbers):
        count = 0
        for i in range(len(numbers) - 1):
            if numbers[i + 1] > numbers[i]:
                count += 1
        return count

    def solve_part_1(self, raw_input):
        numbers = self._get_numbers(raw_input)
        return self._count_increases(numbers)

    def solve_part_2(self, raw_input):
        numbers = self._get_numbers(raw_input)
        sums = [sum(subset) for subset in get_subsets_in_sequence(numbers, 3)]
        return self._count_increases(sums)

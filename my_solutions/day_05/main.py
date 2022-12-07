import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from collections import Counter


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input):
        lines = self._get_input(raw_input)
        return self._count_points(lines)

    def solve_part_2(self, raw_input):
        lines = self._get_input(raw_input)
        return self._count_points(lines, include_diagonals=True)

    def _get_input(self, raw_input):
        return [lib.Line(string, " -> ") for string in raw_input]

    def _count_points(self, lines, include_diagonals=False):
        diagram_counts = Counter()
        for line in lines:
            if line.is_diagonal() and not include_diagonals:
                continue
            for point in line.list_points():
                diagram_counts[point] += 1
        return sum(1 for count in diagram_counts.values() if count > 1)

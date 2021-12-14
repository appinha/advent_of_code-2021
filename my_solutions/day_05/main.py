from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import Coordinates2D, Line
from pprint import pprint
import re
from collections import Counter


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.lines = [Line(string, " -> ") for string in raw_input]

    def _count_points(self, lines, include_diagonals=False):
        diagram_counts = Counter()
        for line in lines:
            if line.is_diagonal() and not include_diagonals:
                continue
            for point in line.get_points():
                diagram_counts[point] += 1
        return sum(1 for count in diagram_counts.values() if count > 1)

    def solve_part_1(self):
        return self._count_points(self.lines)

    def solve_part_2(self):
        return self._count_points(self.lines, include_diagonals=True)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
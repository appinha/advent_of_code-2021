from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import Coordinates2D
from pprint import pprint
import re
from collections import Counter


delimiter = "\n"


class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.start} -> {self.end}"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.lines = self._get_lines(raw_input)

    def _get_lines(self, raw_input):
        lines = []
        for string in raw_input:
            numbers = list(map(int, re.findall(r'\d+', string)))
            lines.append(Line(Coordinates2D(numbers[0:2]), Coordinates2D(numbers[2:])))
        return lines

    def _is_diagonal(self, line):
        return line.start.x != line.end.x and line.start.y != line.end.y

    def _get_line_points(self, line):
        x = [line.start.x, line.end.x]
        y = [line.start.y, line.end.y]

        if len(set(x)) == 1:
            return [(line.start.x, y) for y in range(min(y), max(y) + 1)]
        if len(set(y)) == 1:
            return [(x, line.start.y) for x in range(min(x), max(x) + 1)]

        points = []
        while min(x) < max(x):
            points.append((x[0], y[0]))
            x[0] = x[0] + 1 if x[0] < x[1] else x[0] - 1
            y[0] = y[0] + 1 if y[0] < y[1] else y[0] - 1
        points.append((x[1], y[1]))
        return points

    def _count_points(self, lines, include_diagonals=False):
        diagram_counts = Counter()
        for line in lines:
            if self._is_diagonal(line) and not include_diagonals:
                continue
            for point in self._get_line_points(line):
                diagram_counts[point] += 1
        return sum(1 for count in diagram_counts.values() if count > 1)

    def solve_part_1(self):
        return self._count_points(self.lines)

    def solve_part_2(self):
        return self._count_points(self.lines, include_diagonals=True)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import get_subsets_in_sequence
from pprint import pprint


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.numbers = list(map(int, raw_input))

    def _count_increases(self, numbers):
        count = 0
        for i in range(len(numbers) - 1):
            if numbers[i + 1] > numbers[i]:
                count += 1
        return count

    def solve_part_1(self):
        return self._count_increases(self.numbers)

    def solve_part_2(self):
        sums = [sum(subset) for subset in get_subsets_in_sequence(self.numbers, 3)]
        return self._count_increases(sums)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
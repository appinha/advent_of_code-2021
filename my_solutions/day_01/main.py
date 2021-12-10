from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.numbers = list(map(int, raw_input))

    def _count_increases(self, numbers):
        prev = numbers[0]
        count = 0
        for number in numbers[1:]:
            if number > prev:
                count += 1
            prev = number
        return count

    def solve_part_1(self):
        return self._count_increases(self.numbers)

    def solve_part_2(self):
        sums = [sum(self.numbers[i:i + 3]) for i in range(len(self.numbers) - 2)]
        return self._count_increases(sums)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
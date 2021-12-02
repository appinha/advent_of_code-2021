from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input):
        return list(map(int, raw_input))

    def _count_increases(self, numbers):
        prev = numbers[0]
        count = 0
        for number in numbers[1:]:
            if number > prev:
                count += 1
            prev = number
        return count

    def solve_part_1(self, raw_input):
        numbers = self._get_input(raw_input)
        return self._count_increases(numbers)

    def solve_part_2(self, raw_input):
        numbers = self._get_input(raw_input)
        sums = [sum(numbers[i:i + 3]) for i in range(len(numbers) - 2)]
        return self._count_increases(sums)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint


delimiter = ""


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        pass

    def solve_part_1(self):
        return

    def solve_part_2(self):
        return


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
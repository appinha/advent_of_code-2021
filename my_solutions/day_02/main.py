from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint


delimiter = "\n"


class Command():
    def __init__(self, direction, units):
        self.direction = direction
        self.units = int(units)


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.commands = [Command(*line.split()) for line in raw_input]

    def solve_part_1(self):
        horizontal = 0
        depth = 0
        for command in self.commands:
            if command.direction == 'forward':
                horizontal += command.units
            elif command.direction == 'down':
                depth += command.units
            elif command.direction == 'up':
                depth -= command.units
        return horizontal * depth

    def solve_part_2(self):
        aim = 0
        horizontal = 0
        depth = 0
        for command in self.commands:
            if command.direction == 'forward':
                horizontal += command.units
                depth += aim * command.units
            elif command.direction == 'down':
                aim += command.units
            elif command.direction == 'up':
                aim -= command.units
        return horizontal * depth


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
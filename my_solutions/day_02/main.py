from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint


delimiter = "\n"


class Command():
    def __init__(self, direction, units):
        self.direction = direction
        self.units = units


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input):
        commands = []
        for line in raw_input:
            direction, increase = line.split()
            commands.append(Command(direction, int(increase)))
        return commands

    def solve_part_1(self, raw_input):
        commands = self._get_input(raw_input)
        horizontal = 0
        depth = 0
        for command in commands:
            if command.direction == 'forward':
                horizontal += command.units
            if command.direction == 'down':
                depth += command.units
            if command.direction == 'up':
                depth -= command.units
        return horizontal * depth

    def solve_part_2(self, raw_input):
        commands = self._get_input(raw_input)
        aim = 0
        horizontal = 0
        depth = 0
        for command in commands:
            if command.direction == 'forward':
                horizontal += command.units
                depth += aim * command.units
            if command.direction == 'down':
                aim += command.units
            if command.direction == 'up':
                aim -= command.units
        return horizontal * depth


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
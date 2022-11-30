import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input):
        commands = self._get_input(raw_input)
        horizontal = 0
        depth = 0
        for command in commands:
            if command.direction == 'forward':
                horizontal += command.units
            elif command.direction == 'down':
                depth += command.units
            elif command.direction == 'up':
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
            elif command.direction == 'down':
                aim += command.units
            elif command.direction == 'up':
                aim -= command.units
        return horizontal * depth

    def _get_input(self, raw_input):
        return [Command(*line.split()) for line in raw_input]


class Command():
    def __init__(self, direction, units):
        self.direction = direction
        self.units = int(units)

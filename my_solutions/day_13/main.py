import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from aoc_lib import X, Y, Coord2D
import re


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n\n"

    def solve_part_1(self, raw_input):
        instructions, dot_coordinates = self._get_input(raw_input)
        return len(self._follow_instruction(instructions[0], dot_coordinates))

    def solve_part_2(self, raw_input):
        instructions, dot_coordinates = self._get_input(raw_input)
        final_dot_coordinates = self._follow_instructions(instructions, dot_coordinates)
        self._print_grid(final_dot_coordinates)
        return "HGAJBEHC"

    def _get_input(self, raw_input):
        def transform_input(raw_input, transform):
            return [transform(line) for line in raw_input.split("\n")]

        dot_coordinates = transform_input(raw_input[0], Coord2D.get)
        instructions = transform_input(raw_input[1], self._get_instruction)
        return instructions, dot_coordinates

    def _get_instruction(self, string):
        split = re.search(r'fold along ([a-z])=(\d+)', string)
        return FoldingInstruction(split.group(1), int(split.group(2)))

    def _follow_instruction(self, instruction, dot_coordinates):

        def get_mirrored_coord(coord):
            return (2 * instruction.value) - coord

        new_dot_coordinates = set()
        for coord in dot_coordinates:
            if instruction.axis == 'x' and coord[X] > instruction.value:
                coord = ((get_mirrored_coord(coord[X]), coord[Y]))
            if instruction.axis == 'y' and coord[Y] > instruction.value:
                coord = ((coord[X], get_mirrored_coord(coord[Y])))
            new_dot_coordinates.add(coord)
        return new_dot_coordinates

    def _follow_instructions(self, instructions, dot_coordinates):
        for instruction in instructions:
            dot_coordinates = self._follow_instruction(instruction, dot_coordinates)
        return dot_coordinates

    def _print_grid(self, dot_coordinates):
        max_x, max_y = Coord2D.max(dot_coordinates)
        for y in range(max_y + 1):
            print(*[' #'[(x, y) in dot_coordinates] for x in range(max_x + 1)])


class FoldingInstruction():
    def __init__(self, axis, value):
        self.axis = axis
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.axis}={self.value}"

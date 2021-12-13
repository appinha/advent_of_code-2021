from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import X, Y, Coordinates2D
from pprint import pprint
import re


delimiter = "\n\n"


class FoldingInstruction():
    def __init__(self, axis, value):
        self.axis = axis
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.axis}={self.value}"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.dot_coordinates = self._get_input(raw_input[0], Coordinates2D.get_tuple_from_string)
        self.instructions = self._get_input(raw_input[1], self._get_instruction)

    def _get_input(self, raw_input, transform):
        return [transform(line) for line in raw_input.split("\n")]

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
        max_x, max_y = Coordinates2D.get_max_from_tuples(dot_coordinates)
        for y in range(max_y + 1):
            print(*[' #'[(x, y) in dot_coordinates] for x in range(max_x + 1)])

    def solve_part_1(self):
        return len(self._follow_instruction(self.instructions[0], self.dot_coordinates))

    def solve_part_2(self):
        final_dot_coordinates = self._follow_instructions(self.instructions, self.dot_coordinates)
        self._print_grid(final_dot_coordinates)
        return len(final_dot_coordinates)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import Counter


delimiter = ","


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input):
        return list(map(int, raw_input))

    def _get_total_fuel_cost(self, target, positions, new_rate=False):

        def calculate_cost(target, position, new_rate=False):
            diff = abs(target - position)
            if new_rate:
                return (diff * (diff + 1)) // 2
            return diff

        return sum(calculate_cost(target, position, new_rate) for position in positions)

    def _get_min_fuel_cost(self, raw_input, new_rate=False):
        positions = self._get_input(raw_input)
        total_fuel_costs = [
            self._get_total_fuel_cost(target, positions, new_rate)
            for target in range(min(positions), max(positions))
        ]
        return min(total_fuel_costs)

    def solve_part_1(self, raw_input):
        return self._get_min_fuel_cost(raw_input)

    def solve_part_2(self, raw_input):
        return self._get_min_fuel_cost(raw_input, new_rate=True)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
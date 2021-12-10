from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import Counter


delimiter = ","


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.positions = list(map(int, raw_input))

    def _get_total_fuel_cost(self, target, positions, new_rate=False):

        def calculate_cost(target, position, new_rate=False):
            diff = abs(target - position)
            if new_rate:
                return (diff * (diff + 1)) // 2
            return diff

        return sum(calculate_cost(target, position, new_rate) for position in positions)

    def _get_min_fuel_cost(self, new_rate=False):
        total_fuel_costs = [
            self._get_total_fuel_cost(target, self.positions, new_rate)
            for target in range(min(self.positions), max(self.positions))
        ]
        return min(total_fuel_costs)

    def solve_part_1(self):
        return self._get_min_fuel_cost()

    def solve_part_2(self):
        return self._get_min_fuel_cost(new_rate=True)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
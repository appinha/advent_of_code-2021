import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ","

    def solve_part_1(self, raw_input):
        positions = self._get_input(raw_input)
        return self._get_min_fuel_cost(positions)

    def solve_part_2(self, raw_input):
        positions = self._get_input(raw_input)
        return self._get_min_fuel_cost(positions, new_rate=True)

    def _get_input(self, raw_input):
        return list(map(int, raw_input))

    def _get_total_fuel_cost(self, target, positions, new_rate=False):

        def calculate_cost(position):
            diff = abs(target - position)
            return (diff * (diff + 1)) // 2 if new_rate else diff

        return sum(calculate_cost(position) for position in positions)

    def _get_min_fuel_cost(self, positions, new_rate=False):
        total_fuel_costs = [
            self._get_total_fuel_cost(target, positions, new_rate)
            for target in range(min(positions), max(positions))
        ]
        return min(total_fuel_costs)

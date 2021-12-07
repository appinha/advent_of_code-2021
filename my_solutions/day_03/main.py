from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import defaultdict, Counter


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_bit_counts(self, raw_input):
        count_by_bit_by_position = defaultdict(lambda: Counter())
        for bin_str in raw_input:
            for i, bit in enumerate(bin_str):
                count_by_bit_by_position[i][bit] += 1
        return count_by_bit_by_position

    def _get_gamma(self, raw_input):
        count_by_bit_by_position = self._get_bit_counts(raw_input)
        gamma = ''
        for count_by_bit in count_by_bit_by_position.values():
            gamma += '0' if count_by_bit['0'] > count_by_bit['1'] else '1'
        return gamma

    def _invert_binary(self, binary_str):
        inverse_str = int(binary_str, 2) ^ (2 ** (len(binary_str) + 1) - 1)
        return bin(inverse_str)[3:]

    def _get_gamma_and_epsilon(self, raw_input):
        gamma = self._get_gamma(raw_input)
        epsilon = self._invert_binary(gamma)
        return gamma, epsilon

    def _get_rating(self, binaries, gas):
        position = 0
        while len(binaries) > 1:
            gamma, epsilon = self._get_gamma_and_epsilon(binaries)
            rate = gamma if gas == 'o2' else epsilon
            binaries = [binary for binary in binaries if binary[position] == rate[position]]
            position += 1
        return binaries[0]

    def solve_part_1(self, raw_input):
        gamma, epsilon = self._get_gamma_and_epsilon(raw_input)
        return int(gamma, 2) * int(epsilon, 2)

    def solve_part_2(self, raw_input):
        o2 = self._get_rating(raw_input, 'o2')
        co2 = self._get_rating(raw_input, 'co2')
        return int(o2, 2) * int(co2, 2)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
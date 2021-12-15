from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import get_subsets_in_sequence, lst_to_str, flatten_list
from pprint import pprint
from collections import Counter


delimiter = "\n\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.template = raw_input[0]
        self.insertion_by_pair = dict(line.split(" -> ") for line in raw_input[1].split("\n"))

    def _apply_pair_insertion_for(self, steps, polymer, insertion_by_pair):
        for _ in range(steps):
            new_polymer = [polymer[0]]
            for subset in get_subsets_in_sequence(polymer, 2):
                new_polymer.append([insertion_by_pair[lst_to_str(subset)], subset[1]])
            polymer = flatten_list(new_polymer)

        counts = Counter(polymer)
        return counts.most_common()[0][1] - counts.most_common()[-1][1]

    def _opt_apply_pair_insertion_for(self, steps, polymer, insertion_by_pair):
        counts = Counter(polymer)
        pair_counts = Counter(map(lst_to_str, get_subsets_in_sequence(self.template, 2)))

        for _ in range(steps):
            new_pair_counts = Counter()
            for pair, count in pair_counts.items():
                insertion = insertion_by_pair[pair]
                counts[insertion] += count
                new_pair_counts[pair[0] + insertion] += count
                new_pair_counts[insertion + pair[1]] += count
            pair_counts = new_pair_counts

        return counts.most_common()[0][1] - counts.most_common()[-1][1]

    def solve_part_1(self):
        return self._apply_pair_insertion_for(10, self.template, self.insertion_by_pair)

    def solve_part_2(self):
        return self._opt_apply_pair_insertion_for(40, self.template, self.insertion_by_pair)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
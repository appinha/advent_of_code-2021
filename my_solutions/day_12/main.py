from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import defaultdict


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.neighbors_by_cave = self._get_map_neighbors_by_cave(raw_input)

    def _get_map_neighbors_by_cave(self, raw_input):
        neighbors_by_cave = defaultdict(set)
        for line in raw_input:
            caves = line.split("-")
            neighbors_by_cave[caves[0]].add(caves[1])
            neighbors_by_cave[caves[1]].add(caves[0])
        return neighbors_by_cave

    def _is_small_cave(self, cave):
        return True if cave.islower() else False

    def _already_visited_twice(self, visited_small_caves):
        if len(set(visited_small_caves)) < len(visited_small_caves):
            return True
        return False

    def _count_paths(self, current_cave, visited_small_caves, can_visit_small_cave_twice=False):
        if current_cave == "end":
            return 1
        if current_cave in visited_small_caves:
            if can_visit_small_cave_twice:
                if current_cave == "start" or self._already_visited_twice(visited_small_caves):
                    return 0
            else:
                return 0
        if self._is_small_cave(current_cave):
            visited_small_caves = visited_small_caves + [current_cave]
        return sum(
            self._count_paths(neighbor, visited_small_caves, can_visit_small_cave_twice)
            for neighbor in self.neighbors_by_cave[current_cave]
        )

    def solve_part_1(self):
        return self._count_paths("start", [])

    def solve_part_2(self):
        return self._count_paths("start", [], can_visit_small_cave_twice=True)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
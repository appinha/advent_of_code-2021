import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from collections import defaultdict


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input):
        neighbors_by_cave = self._get_map_neighbors_by_cave(raw_input)
        return self._count_paths(neighbors_by_cave, "start", [])

    def solve_part_2(self, raw_input):
        neighbors_by_cave = self._get_map_neighbors_by_cave(raw_input)
        return self._count_paths(neighbors_by_cave, "start", [], can_visit_small_cave_twice=True)

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

    def _count_paths(
        self,
        neighbors_by_cave,
        current_cave,
        visited_small_caves,
        can_visit_small_cave_twice=False
    ):
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
            self._count_paths(neighbors_by_cave, neighbor, visited_small_caves, can_visit_small_cave_twice)
            for neighbor in neighbors_by_cave[current_cave]
        )

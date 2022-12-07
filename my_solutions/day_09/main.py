import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from aoc_lib import X, Y
from collections import defaultdict
import numpy as np


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"
        self.relative_adjs = [
            (x, y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if not (x == 0 and y == 0) and abs(x) != abs(y)
        ]

    def solve_part_1(self, raw_input):
        self._get_input(raw_input)
        return self._find_risk_level()

    def solve_part_2(self, raw_input):
        self._get_input(raw_input)
        basin_sizes = sorted(self._get_basin_sizes())
        return lib.prod(basin_sizes[-3:])

    def _get_input(self, raw_input):
        self.map_size = (len(raw_input[0]), len(raw_input))
        self.height_by_position = self._get_height_by_position(raw_input)

    def _get_height_by_position(self, raw_input):
        height_by_position = defaultdict(int)
        x, y = 0, 0
        for line in raw_input:
            for height in line:
                height_by_position[(x, y)] = int(height)
                x += 1
            x = 0
            y += 1
        return height_by_position

    def _get_adjacents(self, pos):

        def pos_is_in_map(pos):
            return (0 <= pos[X] < self.map_size[X]) and (0 <= pos[Y] < self.map_size[Y])

        absolute_adjs = [(adj[X] + pos[X], adj[Y] + pos[Y]) for adj in self.relative_adjs]
        return [adj for adj in absolute_adjs if pos_is_in_map(adj)]

    def _is_low_point(self, pos):
        adjacents = self._get_adjacents(pos)
        return all([self.height_by_position[a] > self.height_by_position[pos] for a in adjacents])

    def _find_risk_level(self):
        return sum(
            1 + self.height_by_position[pos]
            for pos in self.height_by_position
            if self._is_low_point(pos)
        )

    def _get_basin_sizes(self):

        def get_low_points():
            return [pos for pos in self.height_by_position if self._is_low_point(pos)]

        def get_basin_size(low_point):
            low_point_height = self.height_by_position[low_point]
            basin_points = [low_point]
            points_queue = [low_point]

            while points_queue:
                pos = points_queue.pop(0)
                for adj in self._get_adjacents(pos):
                    adj_height = self.height_by_position[adj]
                    if (adj_height != 9) and (adj_height > low_point_height) \
                        and (adj not in basin_points):
                        basin_points.append(adj)
                        points_queue.append(adj)
            return len(basin_points)

        return [get_basin_size(low_point) for low_point in get_low_points()]

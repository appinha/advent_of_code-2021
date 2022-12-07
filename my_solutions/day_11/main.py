import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from aoc_lib import NumpyGrid, ROW, COL
import numpy as np


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""
        self.relative_adjs = [
            (x, y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if not (x == 0 and y == 0)
        ]

    def solve_part_1(self, raw_input):
        grid = self._get_input(raw_input)
        return self._simulate_for(100, grid)

    def solve_part_2(self, raw_input):
        grid = self._get_input(raw_input)
        return self._simulate_until_synchronizing(grid)

    def _get_input(self, raw_input):
        return NumpyGrid.from_string(raw_input, int, lambda row: list(row))

    def _get_adjacents(self, grid, pos):

        def pos_is_in_map(pos):
            return (0 <= pos[ROW] < grid.shape[ROW]) and (0 <= pos[COL] < grid.shape[COL])

        absolute_adjs = [(adj[ROW] + pos[ROW], adj[COL] + pos[COL]) for adj in self.relative_adjs]
        return [adj for adj in absolute_adjs if pos_is_in_map(adj)]

    def _flash(self, grid):
        flashes = 0
        flashed = []
        indexes = NumpyGrid.list_index_tuples_where(np.where(grid > 9))
        while indexes:
            for index in indexes:
                flashed.append(index)
                for adj in self._get_adjacents(grid, index):
                    if grid[adj[ROW], adj[COL]] != 0:
                        grid[adj[ROW], adj[COL]] += 1
            for row, col in flashed:
                grid[row, col] = 0
            indexes = NumpyGrid.list_index_tuples_where(np.where(grid > 9))
        flashes += len(NumpyGrid.list_index_tuples_where(np.where(grid == 0)))
        return flashes

    def _simulate_for(self, steps, grid):
        flashes = 0
        while steps:
            grid += 1
            flashes += self._flash(grid)
            steps -= 1
        return flashes

    def _simulate_until_synchronizing(self, grid):
        step = 0
        flashes = 0
        while flashes < grid.size:
            grid += 1
            flashes = self._flash(grid)
            step += 1
        return step

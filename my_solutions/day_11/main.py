from puzzle_solver import PuzzleSolver, run_puzzle_solver
from helpers import Grid
from pprint import pprint
import numpy as np


delimiter = ""


ROW = 0
COL = 1


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)
        self.relative_adjs = [
            (x, y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if not (x == 0 and y == 0)
        ]

    def get_input(self, raw_input):
        self.grid = Grid.get_from_string(raw_input, int, lambda row: list(row))
        self.grid_size = self.grid.shape

    def _get_adjacents(self, pos):

        def pos_is_in_map(pos):
            return (0 <= pos[ROW] < self.grid_size[ROW]) and (0 <= pos[COL] < self.grid_size[COL])

        absolute_adjs = [(adj[ROW] + pos[ROW], adj[COL] + pos[COL]) for adj in self.relative_adjs]
        return [adj for adj in absolute_adjs if pos_is_in_map(adj)]

    def _flash(self, grid):
        flashes = 0
        flashed = []
        indexes = Grid.get_index_tuples_where(np.where(grid > 9))
        while indexes:
            for index in indexes:
                flashed.append(index)
                for adj in self._get_adjacents(index):
                    if grid[adj[ROW], adj[COL]] != 0:
                        grid[adj[ROW], adj[COL]] += 1
            for row, col in flashed:
                grid[row, col] = 0
            indexes = Grid.get_index_tuples_where(np.where(grid > 9))
        flashes += len(Grid.get_index_tuples_where(np.where(grid == 0)))
        return flashes

    def _simulate_for(self, steps):
        flashes = 0
        while steps:
            self.grid += 1
            flashes += self._flash(self.grid)
            steps -= 1
        return flashes

    def _simulate_until_synchronizing(self):
        step = 0
        flashes = 0
        while flashes < self.grid.size:
            self.grid += 1
            flashes = self._flash(self.grid)
            step += 1
        return step


    def solve_part_1(self):
        return self._simulate_for(100)

    def solve_part_2(self):
        return self._simulate_until_synchronizing()


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
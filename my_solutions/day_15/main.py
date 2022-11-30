import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from helpers import X, Y, Grid, sum_tuple_values, get_key_with_min_value
import heapq


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""
        self.rel_neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def solve_part_1(self, raw_input):
        risk_map = self._get_input(raw_input)
        return self._find_lowest_total_risk(risk_map)

    def solve_part_2(self, raw_input):
        risk_map = self._get_input(raw_input)
        full_risk_map = self._get_full_map(risk_map, 5)
        return self._opt_find_lowest_total_risk(full_risk_map)

    def _get_input(self, raw_input):
        return Grid.get_hashmap_from_string(raw_input, int, lambda row: list(row))

    def _get_neighbours(self, coord, shape):
        neighbours = [sum_tuple_values(coord, rel_n) for rel_n in self.rel_neighbours]
        return [n for n in neighbours if Grid.has_position(n, shape)]

    def _find_lowest_total_risk(self, risk_map):
        '''Implementation of Dijkstra's shortest path algorithm as explained in:
        https://youtu.be/pVfj6mxhdMw'''
        shape = Grid.get_hashmap_shape(risk_map)
        unvisited = list(risk_map.keys())
        lowest_risk_by_coord = {coord: float('inf') for coord in unvisited}
        lowest_risk_by_coord[(0, 0)] = 0
        previous_by_coord = {}

        while unvisited:
            current = get_key_with_min_value(lowest_risk_by_coord)
            unvisited.remove(current)
            for n in self._get_neighbours(current, shape):
                if n not in lowest_risk_by_coord: # means n was already visited
                    continue
                prev_risk = lowest_risk_by_coord[n]
                new_risk = risk_map[n] + lowest_risk_by_coord[current]
                if new_risk < prev_risk:
                    lowest_risk_by_coord[n] = int(new_risk)
                    previous_by_coord[n] = current
            del lowest_risk_by_coord[current] # visited

        reversed_path = []
        current = max(risk_map)
        while current != (0, 0):
            reversed_path.append(risk_map[current])
            current = previous_by_coord[current]
        return sum(reversed_path)

    def _opt_find_lowest_total_risk(self, risk_map):
        shape = Grid.get_hashmap_shape(risk_map)
        visited = set()
        risk_by_coord = {(0, 0): 0}

        priority_queue = [(0, (0, 0))]
        while priority_queue:
            _, current = heapq.heappop(priority_queue)
            visited.add(current)
            for n in self._get_neighbours(current, shape):
                if n in visited:
                    continue
                new_risk = risk_map[n] + risk_by_coord[current]
                if n not in risk_by_coord or new_risk < risk_by_coord[n]:
                    risk_by_coord[n] = new_risk
                    heapq.heappush(priority_queue, (new_risk, n))

        destiny = max(risk_map)
        return risk_by_coord[destiny]

    def _get_full_map(self, tile_map, qty):
        shape = Grid.get_hashmap_shape(tile_map)

        def get_new_value(new_coord, full_map):
            x = new_coord[X] if new_coord[X] < shape[X] else new_coord[X] - shape[X]
            if new_coord[X] < shape[X]:
                y = new_coord[Y] if new_coord[Y] < shape[Y] else new_coord[Y] - shape[Y]
            else:
                y = new_coord[Y]
            value = full_map[(x, y)]
            return (value + 1) if value != 9 else 1

        full_map = dict(tile_map)
        for y in range(qty * shape[Y]):
            for x in range(qty * shape[X]):
                if (x, y) in tile_map:
                    continue
                full_map[(x, y)] = get_new_value((x, y), full_map)
        return full_map

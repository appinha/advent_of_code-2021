import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from helpers import X, Y, Z, find_all_integers
from collections import namedtuple
import itertools
import numpy as np


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n\n"
        self.orientations = self._get_orientations()

    def solve_part_1(self, raw_input):
        scanners_readings = self._get_scanners_readings(raw_input)
        _, beacons_coords = self._find_coords(scanners_readings)
        return len(beacons_coords)

    def solve_part_2(self, raw_input):
        scanners_readings = self._get_scanners_readings(raw_input)
        scanners_coords, _ = self._find_coords(scanners_readings)
        return max(self._get_manhattan_distances_between_scanners(scanners_coords))

    def _get_orientations(self):
        orientations = []
        for coords in itertools.permutations([0, 1, 2]):
            for sign1 in [1, -1]:
                for sign2 in [1, -1]:
                    sign3 = 1 if (((coords[1] - coords[0]) % 3 == 1) ^ (sign1 != sign2)) else -1
                    orientations.append(
                        Orientation((coords[0], coords[1], coords[2]), (sign1, sign2, sign3)))
        return orientations

    def _get_scanners_readings(self, raw_input):
        scanners_readings = []
        for scanner in raw_input:
            scanner_readings = scanner.split("\n")
            beacons_coords = []
            for reading in scanner_readings[1:]:
                beacons_coords.append(tuple(find_all_integers(reading)))
            scanners_readings.append(beacons_coords)
        return scanners_readings

    def _try_to_align(self, possible_beacons, known_beacons):

        def get_diffs(coords):
            return [
                (x1 - x0, y1 - y0, z1 - z0)
                for (x0, y0, z0), (x1, y1, z1) in zip(coords, coords[1:])
            ]

        for axis in range(3):
            possible_beacons_sorted = sorted(possible_beacons, key = lambda pos: pos[axis])
            known_beacons_sorted = sorted(known_beacons, key = lambda pos: pos[axis])
            possible_diffs = get_diffs(possible_beacons_sorted)
            known_diffs = get_diffs(known_beacons_sorted)
            intersection = set(known_diffs) & set(possible_diffs)
            if intersection:
                diff = intersection.pop()
                xp, yp, zp = possible_beacons_sorted[possible_diffs.index(diff)]
                xk, yk, zk = known_beacons_sorted[known_diffs.index(diff)]
                xs, ys, zs = (xp - xk, yp - yk, zp - zk)
                aligned_beacons = {(x - xs, y - ys, z - zs) for (x, y, z) in possible_beacons}
                if len(known_beacons & aligned_beacons) >= 12:
                    return (xs, ys, zs), aligned_beacons
        return None, None

    def _orient_and_try_to_align(self, beacons_coords, known_beacons):

        def reorient(coords, orientation):
            axis1, axis2, axis3 = orientation.coords
            sign1, sign2, sign3 = orientation.signs
            return (coords[axis1] * sign1, coords[axis2] * sign2, coords[axis3] * sign3)

        for orientation in self.orientations:
            possible_beacons = [reorient(beacon, orientation) for beacon in beacons_coords]
            found_scanner_coords, aligned_beacons_coords = \
                self._try_to_align(possible_beacons, known_beacons)
            if found_scanner_coords:
                return found_scanner_coords, aligned_beacons_coords
        return None, None

    def _find_coords(self, scanners_readings):
        known_scanners_coords = [(0, 0, 0)]
        known_beacons_coords = set(scanners_readings[0])

        scanners_readings = scanners_readings[1:]
        while scanners_readings:
            for beacons_coords in list(scanners_readings):
                found_scanner_coords, aligned_beacons_coords = \
                    self._orient_and_try_to_align(beacons_coords, known_beacons_coords)
                if found_scanner_coords:
                    known_scanners_coords.append(found_scanner_coords)
                    scanners_readings.remove(beacons_coords)
                    known_beacons_coords |= aligned_beacons_coords
                    break
        return known_scanners_coords, known_beacons_coords

    def _get_manhattan_distances_between_scanners(self, scanners_coords):

        def get_manhattan_distance(coords_1, coords_2):
            return sum([abs(coords_1[i] - coords_2[i]) for i in range(len(coords_1))])

        manhattan_distances = []
        for scanner_pair_coords in itertools.combinations(scanners_coords, 2):
            manhattan_distances.append(get_manhattan_distance(*scanner_pair_coords))
        return manhattan_distances


Orientation = namedtuple('Orientation', ['coords', 'signs'])

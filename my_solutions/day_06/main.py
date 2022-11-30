
import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

from collections import Counter


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ","

    def solve_part_1(self, raw_input):
        timers = self._get_input(raw_input)
        return self._spawn_for(timers, 80)

    def solve_part_2(self, raw_input):
        timers = self._get_input(raw_input)
        return self._opt_spawn_for(timers, 256)

    def _get_input(self, raw_input):
        return list(map(int, raw_input))

    def _spawn_for(self, timers, days):
        for _ in range(days):
            new_timers = []
            for timer in timers:
                new_timers += [6, 8] if timer == 0 else [timer - 1]
            timers = new_timers
        return len(new_timers)

    def _opt_spawn_for(self, timers, days):
        count_by_timer = Counter(timers)
        for _ in range(days):
            new_count_by_timer = Counter()
            for timer in count_by_timer:
                if timer == 0:
                    new_count_by_timer[6] += count_by_timer[timer]
                    new_count_by_timer[8] += count_by_timer[timer]
                else:
                    new_count_by_timer[timer - 1] += count_by_timer[timer]
            count_by_timer = new_count_by_timer
        return sum(new_count_by_timer.values())

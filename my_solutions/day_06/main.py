from types import new_class
from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import Counter


delimiter = ","


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input):
        return list(map(int, raw_input))

    def _spawn_for(self, timers, days):
        day = 0
        while day < days:
            new_timers = []
            for timer in timers:
                if timer == 0:
                    new_timers.append(6)
                    new_timers.append(8)
                else:
                    new_timers.append(timer - 1)
            timers = new_timers
            day += 1
        return timers

    def _opt_spawn_for(self, timers, days):
        count_by_timer = Counter()
        for timer in timers:
            count_by_timer[timer] += 1

        day = 0
        while day < days:
            new_count_by_timer = Counter()
            for timer in count_by_timer:
                if timer == 0:
                    new_count_by_timer[6] += count_by_timer[timer]
                    new_count_by_timer[8] += count_by_timer[timer]
                else:
                    new_count_by_timer[timer - 1] += count_by_timer[timer]
            count_by_timer = new_count_by_timer
            day += 1
        return count_by_timer

    def solve_part_1(self, raw_input):
        timers = self._get_input(raw_input)
        timers = self._spawn_for(timers, 80)
        return len(timers)

    def solve_part_2(self, raw_input):
        timers = self._get_input(raw_input)
        count_by_timer = self._opt_spawn_for(timers, 256)
        return sum(count_by_timer.values())


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
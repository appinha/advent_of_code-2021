from types import new_class
from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import Counter


delimiter = ","


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.timers = list(map(int, raw_input))

    def _spawn_for(self, timers, days):
        day = 0
        while day < days:
            new_timers = []
            for timer in timers:
                new_timers += [6, 8] if timer == 0 else [timer - 1]
            timers = new_timers
            day += 1
        return new_timers

    def _opt_spawn_for(self, timers, days):
        count_by_timer = Counter(timers)
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
        return new_count_by_timer

    def solve_part_1(self):
        total_timers = self._spawn_for(self.timers, 80)
        return len(total_timers)

    def solve_part_2(self):
        count_by_timer = self._opt_spawn_for(self.timers, 256)
        return sum(count_by_timer.values())


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n"
        self.char_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
        self.error_score_by_char = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.complete_score_by_char = {')': 1, ']': 2, '}': 3, '>': 4}

    def solve_part_1(self, raw_input):
        return self._get_error_score(raw_input)

    def solve_part_2(self, raw_input):
        return self._get_middle_score(raw_input)

    def _get_line_error_score(self, line):
        stack = []
        for char in line:
            if char in self.char_pairs.keys():
                stack.append(char)
            elif char != self.char_pairs[stack.pop()]:
                return self.error_score_by_char[char]
        return 0

    def _get_line_middle_score(self, line):
        def get_remaining_open(line):
            stack = []
            for char in line:
                if char in self.char_pairs.keys():
                    stack.append(char)
                elif char == self.char_pairs[stack.pop()]:
                    continue
            return stack

        def close_remaining(chars):
            return [self.char_pairs[char] for char in reversed(chars)]

        def calculate_score(chars):
            score = 0
            for char in chars:
                score = (score * 5) + self.complete_score_by_char[char]
            return score

        remaining_open_chars = get_remaining_open(line)
        closing_chars = close_remaining(remaining_open_chars)
        return calculate_score(closing_chars)

    def _get_error_score(self, subsystem):
        return sum(self._get_line_error_score(line) for line in subsystem)

    def _get_middle_score(self, subsystem):
        incomplete_lines = [line for line in subsystem if not self._get_line_error_score(line)]
        middle_scores = sorted([self._get_line_middle_score(line) for line in incomplete_lines])
        return middle_scores[len(middle_scores) // 2]

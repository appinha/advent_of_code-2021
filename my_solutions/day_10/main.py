from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)
        self.char_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
        self.error_score_by_char = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.complete_score_by_char = {')': 1, ']': 2, '}': 3, '>': 4}

    def get_input(self, raw_input):
        self.subsystem = raw_input

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

    def _get_error_score(self):
        return sum(self._get_line_error_score(line) for line in self.subsystem)

    def _get_middle_score(self):
        incomplete_lines = [line for line in self.subsystem if not self._get_line_error_score(line)]
        middle_scores = sorted([self._get_line_middle_score(line) for line in incomplete_lines])
        return middle_scores[len(middle_scores) // 2]

    def solve_part_1(self):
        return self._get_error_score()

    def solve_part_2(self):
        return self._get_middle_score()


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
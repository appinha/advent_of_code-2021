from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
import re
from collections import defaultdict


delimiter = "\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)
        self.digit_by_string = {
            'abcefg':  '0',
            'cf':      '1',
            'acdeg':   '2',
            'acdfg':   '3',
            'bcdf':    '4',
            'abdfg':   '5',
            'abdefg':  '6',
            'acf':     '7',
            'abcdefg': '8',
            'abcdfg':  '9',
        }
        self.all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.all_letters_set = set(self.all_letters)

    def get_input(self, raw_input):
        self.outputs = self._get_outputs(raw_input)
        self.entries = self._get_entries(raw_input)

    def _get_strings(self, raw_input_line):
        return re.findall(r'[a-z]+', raw_input_line)

    def _get_outputs(self, raw_input):
        outputs = []
        for line in raw_input:
            outputs += self._get_strings(line)[-4:]
        return outputs

    def _get_entries(self, raw_input):
        return [self._get_strings(line) for line in raw_input]

    def _get_output_value(self, entry):

        def get_str_by_digit(entry):
            str_by_digit = defaultdict(set)
            for string in entry:
                if len(string) == 2:
                    str_by_digit['1'].add(''.join(sorted(string)))
                if len(string) == 3:
                    str_by_digit['7'].add(''.join(sorted(string)))
                if len(string) == 4:
                    str_by_digit['4'].add(''.join(sorted(string)))
                if len(string) == 6:
                    str_by_digit['0,6,9'].add(''.join(sorted(string)))
            return str_by_digit['1'], str_by_digit['7'], str_by_digit['4'], str_by_digit['0,6,9']

        def get_letters_set(string):
            return set(list(string)[0])

        def get_digit_from_string(letter_by_code, string):
            decoded_string = ''.join(sorted([letter_by_code[code] for code in list(string)]))
            return self.digit_by_string[decoded_string]

        s_1, s_7, s_4, s_0_6_9 = get_str_by_digit(entry)

        a = get_letters_set(s_7) - get_letters_set(s_1)
        c_f = set(list(list(s_1)[0]))
        b_d = get_letters_set(s_4) - get_letters_set(s_1)
        c_d_e = set([list(self.all_letters_set - set(string))[0] for string in s_0_6_9])
        c = c_f.intersection(c_d_e)
        f = c_f - c
        d = b_d.intersection(c_d_e)
        b = b_d - d
        e = c_d_e - c - d
        g = self.all_letters_set - a - b - c - d - e - f

        codes = [list(code)[0] for code in [a, b, c, d, e, f, g]]
        letter_by_code = {code: self.all_letters[i] for i, code in enumerate(codes)}
        digits = [get_digit_from_string(letter_by_code, string) for string in entry[-4:]]
        return int(''.join((digits)))

    def solve_part_1(self):
        return sum(1 for string in self.outputs if len(string) in [2, 3, 4, 7])

    def solve_part_2(self):
        return sum(self._get_output_value(entry) for entry in self.entries)


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
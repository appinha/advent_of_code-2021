import sys
from termcolor import colored


def run_puzzle_solver(DayPuzzleSolver, delimiter):
    input_filename = sys.argv[1]
    part = sys.argv[2]

    puzzle_solver = DayPuzzleSolver(input_filename, delimiter)
    puzzle_solver.print_solution_for(part)


class PuzzleSolver:
    def __init__(self, input_filename, delimiter):
        self.is_test = True if "test" in input_filename else False
        self.raw_input = self._get_raw_input(input_filename, delimiter)

    def _get_raw_input(self, input_filename, delimiter):
        with open(input_filename, 'r') as f:
            input_file = f.read()

        if self.is_test:
            return self._get_tests_raw_input(input_file, delimiter)
        return self._split_raw_input(input_file, delimiter)

    def _split_raw_input(self, input_file, delimiter):
        raw_input = input_file
        if delimiter:
            raw_input = list(map(str, (raw_input.split(delimiter))))
        return raw_input

    def _get_tests_raw_input(self, input_file, delimiter):

        def separate_parts(input):
            parts = input.split("\n\n*-*-*\n\n") if "*-*-*" in input else [input, input]
            return {"1": parts[0], "2": parts[1]}

        def get_tests(raw_tests):
            tests = []
            for raw_test in raw_tests:
                input, solution = raw_test.split("\n:-> solution=")
                test = {
                    "raw_input": self._split_raw_input(input, delimiter),
                    "solution": solution.replace(" <-:", "")
                }
                tests.append(test)
            return tests

        input_by_part = separate_parts(input_file)
        tests_by_part = {}
        for part in input_by_part:
            raw_tests = input_by_part[part].split("\n\n<--->\n\n")
            tests_by_part[part] = get_tests(raw_tests)
        return tests_by_part

    def get_input(self):
        raise NotImplementedError()

    def solve_part_1(self):
        raise NotImplementedError()

    def solve_part_2(self):
        raise NotImplementedError()

    def print_solution_for(self, part):
        solving_function = self.solve_part_1 if part == "1" else self.solve_part_2

        def print_solution(label, raw_input, solution=None):
            self.get_input(raw_input)
            print(
                colored(label, 'cyan'),
                solving_function(),
                colored("(" + str(solution) + ")" if solution else "", 'green')
            )

        if self.is_test:
            for i, test in enumerate(self.raw_input[part]):
                print_solution("Test {} =".format(i + 1), test["raw_input"], test["solution"])
        else:
            print_solution("Solution =", self.raw_input)

import os
import sys
import time
from termcolor import colored


global main_file
global input_file


def solve_puzzles(day, part):
    if "test" in input_file:
        title = ["Running tests", 'red']
    else:
        title = ["Solution(s) for Day {}".format(day), 'green']
    print(
        colored("\n\n*** ", 'yellow'),
        colored(title[0], title[1]),
        colored(" ***\n", 'yellow')
    )

    if part:
        solve_part(part)
    else:
        solve_part('1')
        solve_part('2')
    print()


def solve_part(part):
    print(colored("\n--- Part {} ---\n".format(part), 'magenta'))

    command = " ".join(["python3", main_file, input_file, part])

    start_time = time.time()
    os.system(command)
    print(colored("\nTime:", 'blue'), time.time() - start_time, "\n")


def normalize_day(arg):
    if len(arg) == 1:
        return "0" + arg
    return arg


if __name__ == '__main__':
    day = sys.argv[1]
    input_file = sys.argv[2]
    part = sys.argv[3] if len(sys.argv) > 3 else None

    directory = "day_" + normalize_day(day) + "/"
    main_file = directory + "main.py"
    input_file = directory + input_file

    solve_puzzles(day, part)

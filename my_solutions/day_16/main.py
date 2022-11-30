from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from collections import namedtuple


delimiter = ""


Packet = namedtuple('Packet', ['version', 'type_ID', 'content'])

def hexa_to_bits(hexa_str):
    return "".join(bin(int(char, 16))[2:].zfill(4) for char in hexa_str)

def read(bits, length):
    return "".join(next(bits) for _ in range(length))

def parse_literal(bits):
    value = ''
    while True:
        prefix = read(bits, 1)
        value += read(bits, 4)
        if prefix == '0':
            return int(value, 2)

def parse_operator(bits):
    length_type_ID = read(bits, 1)
    packets = []

    if length_type_ID == "0":
        subpackets_length = int(read(bits, 15), 2)
        subpackets = iter(read(bits, subpackets_length))

    return

def get_packet(bits):
    version = int(read(bits, 3), 2)
    type_ID = int(read(bits, 3), 2)
    content = parse_literal(bits) if type_ID == 4 else parse_operator(bits)
    return Packet(version=version, type_ID=type_ID, content=content)


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def get_input(self, raw_input):
        self.bits = hexa_to_bits(raw_input)

    def solve_part_1(self):
        packet = get_packet(iter(self.bits))
        return

    def solve_part_2(self):
        return


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
import sys; sys.path.insert(0, '..')
import aoc_lib as lib
from pprint import pprint

import numpy as np


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = "\n\n"

    def solve_part_1(self, raw_input):
        numbers, boards = self._get_input(raw_input)
        winning_number, unmarked_winning_board = self._play_bingo(numbers, boards)
        return winning_number * self._sum_unmarked_numbers(unmarked_winning_board)

    def solve_part_2(self, raw_input):
        numbers, boards = self._get_input(raw_input)
        all_winning = self._play_bingo(numbers, boards, get_all=True)
        winning_number, unmarked_winning_board = all_winning[-1]
        return winning_number * self._sum_unmarked_numbers(unmarked_winning_board)

    def _get_input(self, raw_input):
        numbers = list(map(int, raw_input[0].split(',')))
        boards = [lib.NumpyGrid.from_string(board, int) for board in raw_input[1:]]
        return numbers, boards

    def _mark_number_on_board(self, number, board, marked_board):
        index = np.where(board == number)
        marked_board[index] = number
        board[board == number] = -1

    def _board_has_full_array(self, board):
        full_rows = np.all(board >= 0, axis=lib.ROW)
        full_columns = np.all(board >= 0, axis=lib.COL)
        return any(full_rows) or any(full_columns)

    def _play_bingo(self, numbers, boards, get_all=False):
        marked_boards = [lib.NumpyGrid.generate(boards[0].shape, -1) for _ in range(len(boards))]
        winning_board_indexes = []
        all_winning = []
        for number in numbers:

            for i, board in enumerate(boards):
                if i in winning_board_indexes:
                    continue
                self._mark_number_on_board(number, board, marked_boards[i])

            for i, marked_board in enumerate(marked_boards):
                if i in winning_board_indexes:
                    continue
                if self._board_has_full_array(marked_board):
                    if get_all:
                        winning_board_indexes.append(i)
                        all_winning.append((number, boards[i]))
                    else:
                        return number, boards[i]

        return all_winning

    def _sum_unmarked_numbers(self, board):
        board[board == -1] = 0
        return lib.NumpyGrid.sum(board)

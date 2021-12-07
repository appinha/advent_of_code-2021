from puzzle_solver import PuzzleSolver, run_puzzle_solver
from pprint import pprint
from helpers import get_matrix_from_string
import numpy as np


delimiter = "\n\n"


class DayPuzzleSolver(PuzzleSolver):
    def __init__(self, input_file, delimiter):
        PuzzleSolver.__init__(self, input_file, delimiter)

    def _get_input(self, raw_input):
        numbers = list(map(int, raw_input[0].split(',')))
        boards = [get_matrix_from_string(board, int) for board in raw_input[1:]]
        return numbers, boards

    def _mark_number_on_board(self, number, board, marked_board):
        index = np.where(board == number)
        marked_board[index] = number
        board[board == number] = -1

    def _board_has_full_array(self, board):
        full_rows = np.all(board >= 0, axis=1)
        full_columns = np.all(board >= 0, axis=0)
        return any(full_rows) or any(full_columns)

    def _play_bingo(self, numbers, boards, get_all=False):
        marked_boards = [np.full(boards[0].shape, -1) for _ in range(len(boards))]
        winning_board_indexes = []
        results = []
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
                        results.append((number, boards[i]))
                    else:
                        return number, boards[i]

        return results

    def _sum_unmarked_numbers(self, board):
        board[board == -1] = 0
        return np.sum(board)

    def solve_part_1(self, raw_input):
        numbers, boards = self._get_input(raw_input)
        winning_number, unmarked_winning_board = self._play_bingo(numbers, boards)
        unmarked_sum = self._sum_unmarked_numbers(unmarked_winning_board)
        return unmarked_sum * winning_number

    def solve_part_2(self, raw_input):
        numbers, boards = self._get_input(raw_input)
        results = self._play_bingo(numbers, boards, get_all=True)
        winning_number = results[-1][0]
        unmarked_winning_board = results[-1][1]
        unmarked_sum = self._sum_unmarked_numbers(unmarked_winning_board)
        return unmarked_sum * winning_number


if __name__ == '__main__':
    run_puzzle_solver(DayPuzzleSolver, delimiter)
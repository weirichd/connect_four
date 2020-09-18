import numpy as np
import pytest

from connect_four.env import ConnectFourGame
from connect_four.env.connect_four_env import check_four_in_a_row


def test_step():
    under_test = ConnectFourGame()

    expected = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
        ]
    )

    under_test.step(0)

    assert np.array_equal(under_test.board, expected)
    assert under_test.turn == "O"


def test_step_two_turns():
    under_test = ConnectFourGame()

    expected = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
        ]
    )

    under_test.step(0)
    under_test.step(1)

    assert np.array_equal(under_test.board, expected)
    assert under_test.turn == "X"


def test_step_turns_in_same_col():
    under_test = ConnectFourGame()

    expected = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
        ]
    )

    under_test.step(0)
    under_test.step(0)

    assert np.array_equal(under_test.board, expected)
    assert under_test.turn == "X"


def test_error_if_col_full():
    under_test = ConnectFourGame()

    under_test.board = np.array(
        [
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
        ]
    )

    with pytest.raises(ValueError):
        under_test.step(0)


def test_reset():
    under_test = ConnectFourGame()

    expected = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    )

    # Do some stuff
    under_test.step(1)
    under_test.step(2)
    under_test.step(1)
    under_test.step(4)

    under_test.reset()

    assert np.array_equal(under_test.board, expected)


def test_check_four_in_a_row_empty_board():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    )

    expected = 0

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_horizontal_winner():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 2, 2, 2],
        ]
    )

    expected = 1

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_vertical_winner():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
        ]
    )

    expected = 1

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_diagonal_winner():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 0],
            [0, 2, 1, 2, 1, 0, 0],
        ]
    )

    expected = 1

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_off_diagonal_winner():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 2, 0, 0],
            [0, 0, 1, 2, 2, 0, 0],
            [0, 1, 2, 2, 1, 0, 0],
        ]
    )

    expected = 1

    actual = check_four_in_a_row(board)

    assert actual == expected


def test_check_four_in_a_row_player_two_wins():
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 1, 1, 1, 0, 0],
        ]
    )

    expected = 2

    actual = check_four_in_a_row(board)

    assert actual == expected
